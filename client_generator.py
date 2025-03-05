import os
import sys
import re
import yaml
from yamlcore import CoreLoader
import toml
from shutil import rmtree

# Example usage
base_dir = os.getcwd()
openapi_file = os.path.join(base_dir, 'openapi.yaml')
client_root_dir = os.path.join(base_dir, 'packages','iograph_client',)
client_generated_dir = os.path.join(client_root_dir, 'src','iograph_client','generated')

models_root_dir = os.path.join(base_dir, 'packages','iograph_models',)
models_dir = os.path.join(models_root_dir,'src','iograph_models','models')

python_reserved_words = [
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield"
]

def module_class_name_from_name(name: str):
    func = lambda s: s[:1].upper() + s[1:]

    # handle paths that have paranthesis
    if '(' in name:
        pattern = r'([a-zA-Z]*)='
        params_in_paranthesis :list[str] = re.findall(pattern, name)
        name = name[:name.index('(')]
        if params_in_paranthesis:
            name = name + 'With'+ ''.join([func(x) for x in params_in_paranthesis])
        else:
            name = name

    name = name.strip('$')
    name = name.replace('microsoft.graph.','')
    # name = name.replace('()', '')

    # if name starts with a curly brace, we will assume that it is a path parameter
    if name.startswith('{') and name.endswith('}'):
        # remove the curly braces
        name = name[1:-1]
        name = func(name)
        name = 'By'+ name

    name = func(name)

    name = name.split('.')
    name = ''.join([func(x) for x in name])

    name = name.split('-')
    name = ''.join([func(x) for x in name])

    return name

def module_file_name_from_name(name: str):
    func = lambda s: s[:1].lower() + s[1:]
    # handle paths that have paranthesis
    if '(' in name:
        pattern = r'([a-zA-Z]*)='
        params_in_paranthesis :list[str] = re.findall(pattern, name)
        name = name[:name.index('(')]
        if params_in_paranthesis:
            name = name + '_with_'+ '_'.join([x.lower() for x in params_in_paranthesis])
        else:
            name = name

    name = name.strip('$')
    # name = name.replace('()', '')
    name = name.replace('microsoft.graph.','')

    # if name starts with a curly brace, we will assume that it is a path parameter
    if name.startswith('{') and name.endswith('}'):
        # remove the curly braces
        name = name[1:-1]
        name = func(name)
        name = 'by_'+ name

    name = func(name)
    name = name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    name = name.replace('.', '_')
    name = name.replace('-', '_')
    return name

def clean_field_name(name):
    return name.replace('@', '').replace('.', '_').replace('-', '_')

def resolve_ref_in_components(ref, components):
    ref_path = ref.split('/')[1:]  # Split and remove the initial '#'
    ref_obj = components
    for part in ref_path:
        if part == 'components':
            continue
        ref_obj = ref_obj.get(part, {})
    return ref_obj

def get_field_type(prop_schema):
    if 'type' not in prop_schema:
        raise Exception('No type in schema: ' + str(prop_schema))
    
    if prop_schema['type'] == 'string':
        type = 'str'
        if 'format' in prop_schema:
            if prop_schema['format'] == 'date-time':
                type= 'datetime'
            elif prop_schema['format'] == 'uri':
                type = 'str'
            elif prop_schema['format'] == 'uuid':
                type = 'UUID'
        return type

    elif prop_schema['type'] in ['integer', 'number']:
        type = 'int'
        if 'format' in prop_schema and prop_schema['format'] in ['float', 'double']:
            type = 'float'
        if 'format' in prop_schema and prop_schema['format'] in ['int64', 'int32']:
            type = 'int'
        return type

    elif prop_schema['type'] == 'boolean':
        type = 'bool'
        return type

    elif prop_schema['type'] == 'array':
        type= f"list[{get_field_type(prop_schema['items'])}]"
        return type

    elif prop_schema['type'] == 'object':
        raise Exception('Object type in schema: ' + str(prop_schema))
        return 'Dict[str, Any]'
    
def _pydantic_field_type_write(field_model_name:str, field_type:str, nullable:bool =True, as_any: bool = False,is_enum:bool = False, list_ref:bool = False):
    python_builtin_types = ['str', 'int', 'float', 'bool', 'datetime', 'UUID']

    if 'Optional[' in field_type:
            raise Exception(f'Optional[ in field_type not supported for type: {field_type} model_name: {field_model_name}')

    if is_enum:
        field_type = ' | '.join(['str', field_type])

    if list_ref:
        field_type = f'list[{field_type}]'

    if nullable:
        field_type = f'Optional[{field_type}]'

    if as_any:
        field_type = f'SerializeAsAny[{field_type}]'

    return f'{field_type} = Field(alias="{field_model_name}",{"default=None," if nullable else ""})'

def get_model_discriminator(schema):
    discriminator_mapping = {}

    # we only check for discriminator in schema defined for model and not from references
    if 'allOf' in schema:
        for item in schema['allOf']:
            if '$ref' in item:
                continue
            else:
                return get_model_discriminator(item)
    
    if 'discriminator' in schema:
        for key, value in schema['discriminator']['mapping'].items():
            model_name = value.split('/')[-1]
            discriminator_mapping[key] = model_name
            
        discriminator_field = schema['discriminator']['propertyName']
        return discriminator_field, discriminator_mapping
    else:
        return None

def _check_field_type_has_discriminator(model_name, components):

    model_schema = components['schemas'][model_name]

    if not model_schema:
        raise Exception('Model schema not found for model name: ' + model_name)
    
    if 'allOf' in model_schema:
        for item in model_schema['allOf']:
            if 'discriminator' in item:
                return True
    
    else:
        if 'discriminator' in model_schema:
            return True
        else:
            return False

def _check_field_type_is_enum(model_name, components):
    model_schema = components['schemas'][model_name]

    if not model_schema:
        raise Exception('Model schema not found for model name: ' + model_name)
    
    if 'allOf' in model_schema:
        for item in model_schema['allOf']:
            if 'type' in model_schema and 'enum' in model_schema:
                raise Exception('Enum type in allOf schema for model name: ' + model_name)
                return True
            
    if 'type' in model_schema and 'enum' in model_schema:
        return True
    else:
        return False
    
def get_schema_fields(name:str, schema, components,dependencies:list):
    fields = {}

    if 'allOf' in schema:
        for item in schema['allOf']:
            if '$ref' in item:
                model_name = item['$ref'].split('/')[-1]
                resolved_schema = resolve_ref_in_components(item['$ref'], components)
                try:
                    fields.update(get_schema_fields(model_name, resolved_schema, components, dependencies))
                except Exception as e:
                    raise Exception('Error in allOf schema for model name: ' + name)
            else:
                fields.update(get_schema_fields(name, item, components, dependencies))

    # Extract fields from properties
    if 'properties'  in schema:

        # extract fields from properties
        for prop_name, prop_schema in schema['properties'].items():

            if '$ref' in prop_schema:
                model_name = prop_schema['$ref'].split('/')[-1]
                has_discriminator = _check_field_type_has_discriminator(model_name, components)
                is_enum = _check_field_type_is_enum(model_name, components)
                fields[clean_field_name(prop_name)] = _pydantic_field_type_write(
                    field_model_name=prop_name,
                    field_type=module_class_name_from_name(model_name),
                    nullable= prop_schema.get('nullable', True),
                    as_any = has_discriminator,
                    is_enum = is_enum,
                )
                dependencies.append(model_name)
            
            elif 'anyOf' in prop_schema:
                # find the first schema that is a reference
                model_name = None
                for item in prop_schema['anyOf']:
                    if '$ref' in item:
                        model_name = item['$ref'].split('/')[-1]
                        has_discriminator = _check_field_type_has_discriminator(model_name, components)
                        is_enum = _check_field_type_is_enum(model_name, components)
                        fields[clean_field_name(prop_name)] = _pydantic_field_type_write(
                            field_model_name=prop_name,
                            field_type=module_class_name_from_name(model_name),
                            nullable= prop_schema.get('nullable', True),
                            as_any = has_discriminator,
                            is_enum = is_enum,
                        )
                        dependencies.append(model_name)
                        break

                # check if this logic is comprehensive and without exc
                if model_name is None:
                    raise Exception('No reference found in anyOf schema for model name: ' + name)
                    
            elif 'oneOf' in prop_schema:
                field_types = []
                for item in prop_schema['oneOf']:
                    if '$ref' in item:
                        model_name = item['$ref'].split('/')[-1]
                        has_discriminator = _check_field_type_has_discriminator(model_name, components)
                        field_types.append(module_class_name_from_name(model_name))
                        dependencies.append(model_name)
                    else:
                        field_types.append(get_field_type(item))
                # Warning: this is not using the _pydantic_field_type_write function
                fields[clean_field_name(prop_name)] = ' | '.join(field_types)

            elif 'type' in prop_schema:

                # Handle if the property is an array
                if prop_schema['type'] == 'array' and '$ref' in prop_schema['items']:
                    model_name = prop_schema['items']['$ref'].split('/')[-1]
                    has_discriminator = _check_field_type_has_discriminator(model_name, components)
                    is_enum = _check_field_type_is_enum(model_name, components)
                    fields[clean_field_name(prop_name)] = _pydantic_field_type_write(
                        field_model_name=prop_name,
                        field_type=module_class_name_from_name(model_name),
                        nullable = True,
                        as_any= has_discriminator,
                        is_enum = is_enum,
                        list_ref= True,
                    )
                    dependencies.append(model_name)

                elif prop_schema['type'] == 'array' and 'anyOf' in prop_schema['items']:
                    # find the first schema that is a reference
                    model_name = None
                    for item in prop_schema['items']['anyOf']:
                        if '$ref' in item:
                            model_name = item['$ref'].split('/')[-1]
                            dependencies.append(model_name)
                            break

                    # check if this logic is comprehensive and without exc
                    if model_name is None:
                        raise Exception('No reference found in anyOf schema under items for model name: ' + name)
                    else:
                        has_discriminator = _check_field_type_has_discriminator(model_name, components)
                        is_enum = _check_field_type_is_enum(model_name, components)
                        fields[clean_field_name(prop_name)] = _pydantic_field_type_write(
                            field_model_name=prop_name,
                            field_type=module_class_name_from_name(model_name),
                            nullable= True,
                            as_any = has_discriminator,
                            is_enum = is_enum,
                        )
                else:
                    fields[clean_field_name(prop_name)] = _pydantic_field_type_write(
                        field_model_name=prop_name,
                        field_type=get_field_type(prop_schema),
                        nullable= prop_schema.get('nullable', True)
                    )
            else:
                fields[clean_field_name(prop_name)] = _pydantic_field_type_write(
                    field_model_name=prop_name,
                    field_type='str',
                    nullable= prop_schema.get('nullable', True)
                )


    return fields

def _clean_pydantic_field_name(name):
    # name =  name.replace('@', '').replace('.', '_').replace('-', '_')
    if name in python_reserved_words:
        # print(f'Field name {name} is a reserved keyword in python, renaming to {name}_')
        name = f'{name}_'
        return name
    return name

def create_pydantic_model(name:str, schema, components):
    fields = {}
    deps = []

    if any(x in schema for x in ['anyOf', 'oneOf']):
        raise Exception('anyOf and oneOf in model definition not supported yet')

    # if 'properties' in schema:
    fields.update(get_schema_fields(name, schema, components, deps))

    # get discriminator mapping
    discriminator = get_model_discriminator(schema)

    # write to file
    model_file = os.path.join(models_dir, f'{module_file_name_from_name(name)}.py')
    with open(model_file, 'w') as model_file_obj:
        class_name = module_class_name_from_name(name)
        model_file_obj.write(f'from __future__ import annotations\n')
        if any('UUID' in x for x in fields.values() if isinstance(x,str)):
            model_file_obj.write(f'from uuid import UUID\n')
        if any('Optional' in x for x in fields.values() if isinstance(x,str)):
            model_file_obj.write(f'from typing import Optional\n')
        # write discriminator related imports

        if discriminator:
            model_file_obj.write(f'from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError\n')
            model_file_obj.write(f'from typing_extensions import Self\n')
            model_file_obj.write(f'from typing import Any\n')

        if any('datetime' in x for x in fields.values() if isinstance(x,str)):
            model_file_obj.write(f'from datetime import datetime\n')

        model_file_obj.write(f'from pydantic import BaseModel, Field, SerializeAsAny\n')
        model_file_obj.write('\n')
        model_file_obj.write('\n')
        

        model_file_obj.write(f'class {class_name}(BaseModel):\n')
        for field_name, field_type in fields.items():
            model_file_obj.write(f'\t{_clean_pydantic_field_name(field_name)}: {field_type}\n')
        model_file_obj.write(f'\n')

        # write discriminator mapping
        
        if discriminator:
            discriminator_field, discriminator_mapping = discriminator
            model_file_obj.write('\t@model_validator(mode="wrap")\n')
            model_file_obj.write('\tdef convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:\n')
            model_file_obj.write('\t\ttry:\n')
            model_file_obj.write('\t\t\t# check with parent model to catch any errors\n')
            model_file_obj.write('\t\t\tparent_validated_model = handler(data)\n')
            model_file_obj.write('\t\t\t# check if the discriminator field is present\n')
            model_file_obj.write(f'\t\t\tif "{discriminator_field}" not in data:\n')
            model_file_obj.write(f'\t\t\t\treturn parent_validated_model\n')
            model_file_obj.write('\t\t\t# get the discriminator value\n')
            model_file_obj.write(f'\t\t\tmapping_key = data["{discriminator_field}"]\n')            
            for mapping_key, mapping_value in discriminator_mapping.items():
                model_file_obj.write(f'\t\t\tif mapping_key == "{mapping_key}":\n')
                model_file_obj.write(f'\t\t\t\tfrom .{module_file_name_from_name(mapping_value)} import {module_class_name_from_name(mapping_value)}\n')
                model_file_obj.write(f'\t\t\t\treturn {module_class_name_from_name(mapping_value)}.model_validate(data)\n')
            model_file_obj.write('\t\t\traise ValidationError(f"Invalid discriminator value: {mapping_key}")\n')
            model_file_obj.write(f'\n')
            model_file_obj.write('\t\texcept Exception as e:\n')
            model_file_obj.write('\t\t\traise e\n')
            model_file_obj.write('\n')
        
        # write dependency imports
        for dep in deps:
            # Ignore self-referencing dependencies
            if module_class_name_from_name(dep) == class_name:
                continue
            model_file_obj.write(f'from .{module_file_name_from_name(dep)} import {module_class_name_from_name(dep)}\n')
        
        model_file_obj.write(f'\n')

def create_enum_model(name: str, schema, components, enum_type):
    # write to file
    model_file = os.path.join(models_dir, f'{module_file_name_from_name(name)}.py')
    with open(model_file, 'w') as model_file_obj:
        class_name = module_class_name_from_name(name)
        model_file_obj.write(f'from __future__ import annotations\n')
        if enum_type == 'string':
            model_file_obj.write(f'from enum import StrEnum\n')
            model_file_obj.write(f'\n\n')
            model_file_obj.write(f'class {class_name}(StrEnum):\n')
        elif enum_type == 'integer':
            model_file_obj.write(f'from enum import IntEnum\n')
            model_file_obj.write(f'\n\n')
            model_file_obj.write(f'class {class_name}(IntEnum):\n')
        for field_name in schema['enum']:

            if field_name in python_reserved_words:
                field_name = f'{field_name}_'
            if field_name.startswith('-'):
                field_name = field_name.replace('-', '_')
                
            model_file_obj.write(f'\t{field_name} = "{field_name}"\n')
        model_file_obj.write(f'\n')

def create_root_model(name: str, schema, components):
    # write to file
    model_file = os.path.join(models_dir, f'{module_file_name_from_name(name)}.py')
    field_type = get_field_type(schema)
    with open(model_file, 'w') as model_file_obj:
        class_name = module_class_name_from_name(name)
        model_file_obj.write(f'from __future__ import annotations\n')
        model_file_obj.write(f'from pydantic import RootModel\n')
        model_file_obj.write(f'\n\n')
        model_file_obj.write(f'{class_name} = RootModel[{field_type}]\n')
                                      
def create_model(name: str, schema, components):
    if 'type' in schema and schema['type'] == 'object':
        create_pydantic_model(name, schema, components)

    elif 'type' in schema and schema['type'] in ['integer', 'number', 'boolean','string']:

        if 'enum' in schema:
            if schema['type'] == 'integer':
                create_enum_model(name, schema,components, enum_type='integer')
            elif schema['type'] == 'string':
                create_enum_model(name, schema,components, enum_type='string')
            else: 
                raise Exception('Model type enum but not string or integer not supported in create_model : ' + name)
        else:
            create_root_model(name, schema, components)

    elif 'allOf' in schema:
        create_pydantic_model(name, schema, components)

    else:
        print(name)
        print(schema)
        raise Exception('Model type not supported in create_model : ' + name)



def resolve_responses(responses:dict, path: str, method: str,components:dict) -> tuple[dict, set]:
    response_dict = {}
    dependencies = set()
    for status, response in responses.items():
        # non-specific status codes
        if status in ['2XX',]:

            if '$ref' in response:
                model_name = response['$ref'].split('/')[-1]
                response_dict[status] = module_class_name_from_name(model_name)
                dependencies.add(model_name)
            
            elif 'content' in response:
                content = response['content']
                if 'application/json' in content:
                    schema = content['application/json']['schema']
                    
                    if '$ref' in schema:
                        model_name = schema['$ref'].split('/')[-1]
                        response_dict[status] = module_class_name_from_name(model_name)
                        dependencies.add(model_name)
                    
                    elif 'anyOf' in schema:
                        # find the first schema that is a reference
                        model_name = None
                        for item in schema['anyOf']:
                            if '$ref' in item:
                                model_name = item['$ref'].split('/')[-1]
                                dependencies.add(model_name)
                                response_dict[status] = module_class_name_from_name(model_name)
                                break
                        if model_name is None:
                            raise Exception('No reference found in anyOf schema for response: ' + str(path+' method: '+method))
                    
                    elif 'type' in schema and schema['type'] == 'string':
                        if 'format' in schema and schema['format'] == 'binary':
                            response_dict[status] = 'bytes'
                        elif 'format' in schema and schema['format'] == 'byte':
                            response_dict[status] = 'bytes'
                        elif 'format' in schema and schema['format'] == 'date-time':
                            response_dict[status] = 'datetime'
                        else:
                            response_dict[status] = 'str'

                    elif 'type' in schema and schema['type'] == 'object':

                        model_name = path.split('/')[-1] + method.capitalize() + 'Response'
                        create_model(model_name, schema, components)
                        response_dict[status] = module_class_name_from_name(model_name)
                        dependencies.add(model_name)
                    
                    elif 'type' in schema and schema['type'] == 'array':
                        if '$ref' in schema['items']:
                            model_name = schema['items']['$ref'].split('/')[-1]
                            response_dict[status] = f'list[{module_class_name_from_name(model_name)}]'
                            dependencies.add(model_name)
                        else:
                            raise Exception('Array without reference in response: ' + str(path+' method: '+method))
                    else:
                        raise Exception('Response without application/json/schema/reference in response: ' + str(path+' method: '+method))
                
                elif 'application/octet-stream' in content:
                    response_dict[status] = 'bytes'
                
                elif any(x in content for x in ['image/bmp', 'image/jpg', 'image/jpeg', 'image/png', 'image/gif','image/tiff','image/vnd.microsoft.icon']):
                    response_dict[status] = 'bytes'
               
                else:
                    raise Exception('Response without response-type in response: ' + str(path+' method: '+method))
            
            elif 'description' in response and response['description'] == 'Success':
                response_dict[status] = 'None'
            
            else:
                raise Exception('Response without reference in response: ' + str(path+' method: '+method))
        
        elif status == '204':
            response_dict[status] = 'None'
        elif status in ['4XX', '5XX']:
            response_dict[status] = module_class_name_from_name('microsoft.graph.ODataErrors.ODataError')
            dependencies.add('microsoft.graph.ODataErrors.ODataError')
    return response_dict, dependencies

def resolve_request_body(request_body:dict, path:str, method:str, components:dict) -> tuple[str, set]:
    
    if '$ref' in request_body:
        model_name = request_body['$ref'].split('/')[-1]
        schema = resolve_ref_in_components(request_body['$ref'], components)
        if 'content' in schema:
            return resolve_request_body(schema, path, method, components)
        create_model(model_name, schema, components)
        return module_class_name_from_name(model_name), {model_name}
    if 'content' not in request_body:
        raise Exception('No content in request body for path: ' + path + ' method: ' + method)
    content = request_body['content']
    
    if 'application/json' in content:
        schema = content['application/json']['schema']
        if '$ref' in schema:
            model_name = schema['$ref'].split('/')[-1]
            return module_class_name_from_name(model_name), {model_name}
        elif 'type' in schema and schema['type'] == 'string':
            return 'str', set()
        elif 'type' in schema and schema['type'] == 'object':
            model_name = path.split('/')[-1] + method.capitalize() + 'Request'
            create_model(model_name, schema, components)
            return module_class_name_from_name(model_name), {model_name}

        elif 'type' in schema and schema['type'] == 'array':
            if '$ref' in schema['items']:
                model_name = schema['items']['$ref'].split('/')[-1]
                return f'list[{module_class_name_from_name(model_name)}]', {model_name}
            else:
                raise Exception('Array without reference in request body for path: ' + path + ' method: ' + method)
        else:
            raise Exception('No reference in schema for request body for path: ' + path + ' method: ' + method)
    
    elif 'application/octet-stream' in content:
        return 'bytes', set()
    elif any(x in content for x in ['image/bmp', 'image/jpg', 'image/jpeg', 'image/png', 'image/gif','image/tiff','image/vnd.microsoft.icon']):
        return 'bytes', set()
               
    else:
        raise Exception('No request body schema for path: ' + path + ' method: ' + method)

def url_safe_param_name(name:str):
    name = name.replace('$', '%24')
    name = name.replace('@', '%40')
    name = name.replace('.', '%2E')
    name = name.replace('-', '%2D')
    return name

def clean_param_name(name):

    return name.strip('$').replace('@', '').replace('.', '_').replace('-', '_')

def resolve_path_parameters(path_parameters:list, components:dict):
    fields = {}
    if path_parameters:
        for param in path_parameters:
            if 'in' not in param or param['in'] != 'path':
                raise Exception('Path parameter without in=path: ' + str(param))
            # check if required is set
            if 'required' not in param:
                raise Exception('Path parameter without required: ' + str(param))
            if '$ref' in param:
                resolved_param = resolve_ref_in_components(param['$ref'], components)
                fields[clean_param_name(resolved_param["name"])] = resolved_param
            else:
                fields[clean_param_name(param["name"])] = param
    return fields

def get_param_field_type(param):
    if 'schema' in param:
        schema = param['schema']
        if '$ref' in schema:
            return 'str'
        elif 'anyOf' in schema:
            return 'str'
        else:
            return get_field_type(schema)

    else:
        raise Exception('No schema in parameter: ' + str(param))

def _query_param_writes(query_parameters:list,method:str):
    writes = []
    writes.append(f'\tclass {method[0].upper()+method[1:]}QueryParams(BaseModel):\n')
    for param in query_parameters:
        writes.append(f'\t\t{clean_param_name(param["name"])}: {get_param_field_type(param)} = Field(default=None,serialization_alias="{url_safe_param_name(param["name"])}")\n')

    return writes

def _method_writes(
        method:str,
        details:dict,
        endpoint_path:str,
        path_parameters:list,
        http_path:str,
        components:dict
    ) -> list:

    # for method, details in methods.items():
    import_deps = set()

    # path parameters
    path_params = resolve_path_parameters(path_parameters, components)

    # Query parameters
    query_params = []
    for param in details.get('parameters', []):
        if '$ref' in param:
            resolved_param = resolve_ref_in_components(param['$ref'], components)
            if 'in' in resolved_param and resolved_param['in'] == 'query':
                query_params.append(resolved_param)
        else:
            if 'in' in param and param['in'] == 'query':
                query_params.append(param)
    query_parameters_writes  = _query_param_writes(query_params, method) if query_params else []

    # Header parameters
    header_params = []
    for param in details.get('parameters', []):
        if '$ref' in param:
            resolved_param = resolve_ref_in_components(param['$ref'], components)
            if 'in' in resolved_param and resolved_param['in'] == 'header':
                header_params.append(resolved_param)
        else:
            if 'in' in param and param['in'] == 'header':
                header_params.append(param)

    # Response types
    responses = details.get('responses', {})
    (response_dict, response_dependencies) = resolve_responses(responses, endpoint_path, method, components=components)
    import_deps.update(response_dependencies)

    success_response = None
    if '2XX' in response_dict:
        success_response = response_dict.get('2XX')
    elif '204' in response_dict:
        success_response = response_dict.get('204')
    if not success_response:
        raise Exception('No success response in responses for path: ' + http_path + ' method: ' + method)

    # Request body
    request_body = details.get('requestBody', {})
    if request_body:
        (request_body_type, request_body_dependencies) = resolve_request_body(request_body, endpoint_path, method, components)
        import_deps.update(request_body_dependencies)
    
    # Add tags as a list
    tags = details.get('tags', [])

    # Add externalDocs if available
    external_docs = details.get('externalDocs', {})

    # return values
    dependency_writes = list()
    function_writes = list()


    # Create  Python file descriptor for HTTP method
    
    # write the imports
    for dep in import_deps:
        dependency_writes.append(f'from iograph_models.models.{module_file_name_from_name(dep)} import {module_class_name_from_name(dep)}\n')

    # write the function
    function_writes.append(f'\tasync def {method}(\n')
    function_writes.append(f'\t\tself,\n')

    # Request body if any and optional if not required
    if request_body:
        function_writes.append(f'\t\tbody: {request_body_type}{' = None' if not request_body.get('required',True) else ''},\n')
    
    # Request Config
    if query_parameters_writes:
        function_writes.append(f'\t\trequest_configuration: Optional[RequestConfiguration[{method[0].upper()+method[1:]}QueryParams]] = None,\n')
    else:
        function_writes.append(f'\t\trequest_configuration: Optional[RequestConfiguration[BaseModel]] = None,\n')
    
    function_writes.append(f'\t) -> {success_response}:\n')

    function_writes.append(f'\t\t"""\n')
    function_writes.append(f'\t\t{details.get("summary", "")}\n')
    function_writes.append(f'\t\t{details.get("description", "")}\n')
    if external_docs:
        function_writes.append(f'\t\t{external_docs['description']}: {external_docs['url']}\n')
    function_writes.append(f'\t\t"""\n')
    function_writes.append(f'\t\ttags = {tags}\n')
    if header_params:
        function_writes.append(f'\t\theader_parameters = {header_params}\n')
    function_writes.append('\n')

    # write error mapping
    function_writes.append('\t\terror_mapping: dict[str, type[BaseModel]] = {\n')
    # function_writes.append(f'\t\t\t"4XX": {response_dict.get('4XX')},\n')
    # function_writes.append(f'\t\t\t"5XX": {response_dict.get('5XX')},\n')
    function_writes.append(f'\t\t\t"XXX": ODataErrorsODataError,\n') # hardcoded value, not good
    function_writes.append('\t\t}\n')
    function_writes.append('\n')


    #request information
    function_writes.append('\t\trequest_info: RequestInformation = RequestInformation(\n')
    function_writes.append(f'\t\t\tmethod = Method.{method.upper()},\n')
    function_writes.append('\t\t\turl_template = self.url_template,\n')
    function_writes.append('\t\t\tpath_parameters = self.path_parameters,\n')
    function_writes.append('\t\t)\n')
    function_writes.append('\t\trequest_info.configure(request_configuration)\n')
    function_writes.append('\t\trequest_info.headers.try_add("Accept", "application/json")\n')
    if request_body:
        function_writes.append('\t\trequest_info.set_content(body, "application/json")\n')

    # return statement
    if success_response == 'None':
        function_writes.append('\t\treturn await self.request_adapter.send_no_response_content_async(request_info, error_mapping)\n')
    elif success_response.startswith('list['):
        function_writes.append('\t\treturn await self.request_adapter.send_collection_async(request_info, error_mapping)\n')
    elif success_response in ['bytes','int']:
        function_writes.append(f'\t\treturn await self.request_adapter.send_primitive_async(request_info, "{success_response}", error_mapping)\n')
    else:
        function_writes.append(f'\t\treturn await self.request_adapter.send_async(request_info, {success_response}, error_mapping)\n')


    return dependency_writes, function_writes, query_parameters_writes

def url_safe_string(string:str):
    return string.replace('-', '%2D')

def write_init_file(
        init_file_path, 
        model_name,
        http_path,
        relative_path_to_root: str,
        dependencies:set[str] = None,
        method_functions:list[list[str]] = None,
        query_params:list[list[str]] = None,
        raw_path_param_keys: list[str] = None,
        # endpoint_methods = None, 
        ):
    if not relative_path_to_root:
        raise Exception('Relative path to root is required for init file')
    
    # Quote the http_path
    if raw_path_param_keys:
        for key in raw_path_param_keys:
            
            http_path = http_path.replace(key,url_safe_string(key))


    with open(init_file_path, 'w+b',buffering=0) as init_file_obj:
        init_file_obj.write((f'# Auto-generated client\n\n').encode())
        init_file_obj.write(('from __future__ import annotations\n').encode())
        init_file_obj.write(('from kiota_abstractions.method import Method\n').encode())
        init_file_obj.write(('from kiota_abstractions.base_request_builder import BaseRequestBuilder\n').encode())
        init_file_obj.write(('from kiota_abstractions.base_request_configuration import RequestConfiguration\n').encode())
        init_file_obj.write((f'from {relative_path_to_root}..request_information import RequestInformation\n').encode())
        init_file_obj.write(('from pydantic import BaseModel, Field\n').encode())
        init_file_obj.write(('from typing import Union, Any, Optional\n').encode())
        init_file_obj.write(('from typing import TYPE_CHECKING\n').encode())
        init_file_obj.write(('\n').encode())
        init_file_obj.write(('if TYPE_CHECKING:\n').encode())
        init_file_obj.write((f'\tfrom {relative_path_to_root}..request_adapter import HttpxRequestAdapter\n').encode())

        if dependencies:
            # write the dependencies
            for dep in dependencies:
                init_file_obj.write((dep).encode())

        init_file_obj.write((f'\n\n').encode())

        # write the endpoint class name
        init_file_obj.write((f'class {module_class_name_from_name(model_name)}Request(BaseRequestBuilder):\n').encode())
        init_file_obj.write(('\tdef __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:\n').encode())
        url_template = "{+baseurl}"+http_path
        init_file_obj.write(f'\t\tsuper().__init__(request_adapter, "{url_template}", path_parameters)\n'.encode())
        # init_file_obj.write(('\t\tself.request_adapter = request_adapter\n').encode())
        # init_file_obj.write(('\t\tself.url_template: str = "{+baseurl}'+f'{http_path}"\n').encode())
        # init_file_obj.write((f'\t\tself.path_parameters: dict[str, Any] = path_parameters\n').encode())
        init_file_obj.write(('\n').encode())
        
        if method_functions:
            # write the methods
            for method in method_functions:
                for func in method:
                    init_file_obj.write((func).encode())
                init_file_obj.write(('\n').encode())

        if query_params:
            # write the query parameters
            for query_param in query_params:
                for query in query_param:
                    init_file_obj.write((query).encode())
                init_file_obj.write(('\n').encode())

        # write with_url function
        init_file_obj.write((f'\tdef with_url(self, raw_url: str) -> {module_class_name_from_name(model_name)}Request:\n').encode())
        init_file_obj.write(('\t\t"""\n').encode())
        init_file_obj.write(('\t\tReturns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.\n').encode())
        init_file_obj.write(('\t\tparam raw_url: The raw URL to use for the request builder.\n').encode())
        init_file_obj.write((f'\t\tReturns: {module_class_name_from_name(model_name)}Request\n').encode())
        init_file_obj.write(('\t\t"""\n').encode())
        init_file_obj.write(('\t\tif raw_url is None:\n').encode())
        init_file_obj.write(('\t\t\traise TypeError("raw_url cannot be None.")\n').encode())
        init_file_obj.write((f'\t\treturn {module_class_name_from_name(model_name)}Request(self.request_adapter, self.path_parameters)\n').encode())
        init_file_obj.write(('\n').encode())

def _child_in_parent_writes(parent_file_content: list, model_name: str, child_path_parameters: dict):

    # write the child import statement in type checking block
    # check if import is already in the file
    if not f'\tfrom .{module_file_name_from_name(model_name)} import {module_class_name_from_name(model_name)}Request\n' in parent_file_content:
        # check if TYPE_CHECKING: is already in the file
        if 'if TYPE_CHECKING:\n' not in parent_file_content:
            #find 'from typing import TYPE_CHECKING\n\n' and insert 'if TYPE_CHECKING:\n'
            i = parent_file_content.index('from typing import TYPE_CHECKING\n')
            parent_file_content.insert(i+2, 'if TYPE_CHECKING:\n')
            parent_file_content.insert(i+3, f'\tfrom .{module_file_name_from_name(model_name)} import {module_class_name_from_name(model_name)}Request\n')
        
        else:
            # find the last import statement and insert the import
            i = parent_file_content.index('if TYPE_CHECKING:\n')
            parent_file_content.insert(i+1, f'\tfrom .{module_file_name_from_name(model_name)} import {module_class_name_from_name(model_name)}Request\n')

    # write neccessary imports if child is a path parameter identifier
    # if '{' is in model_name but child_path_parameters is empty, it means although the child model 
    # is a path parameter, it is not a valid path in openapi dict
    if child_path_parameters:
        # Check if get_path_parameters is already in the file
        if not 'from kiota_abstractions.get_path_parameters import get_path_parameters\n' in parent_file_content:
            # find index of __annotations__ and insert the import
            i = parent_file_content.index('from __future__ import annotations\n')
            parent_file_content.insert(i+1, 'from kiota_abstractions.get_path_parameters import get_path_parameters\n')
    
    # write class property
    # check if property is already in the file
    if not f'\tdef {module_file_name_from_name(model_name)}(self,\n' in parent_file_content:
        if not child_path_parameters:
            parent_file_content.append('\t@property\n')
        parent_file_content.append(f'\tdef {module_file_name_from_name(model_name)}(self,\n')

        for param_name, param_schema in child_path_parameters.items():
            parent_file_content.append(f'\t\t{param_name}: {get_param_field_type(param_schema)},\n')
        
        parent_file_content.append(f'\t) -> {module_class_name_from_name(model_name)}Request:\n')
        
        if child_path_parameters:
            # check if path parameters are present
            for param_name, param_schema in child_path_parameters.items():
                parent_file_content.append(f'\t\tif {param_name} is None:\n')
                parent_file_content.append(f'\t\t\traise TypeError("{param_name} cannot be null.")\n')

            parent_file_content.append('\n')
            parent_file_content.append('\t\tpath_parameters = get_path_parameters(self.path_parameters)\n')
            # write path parameters  in dict
            for param_name, param_schema in child_path_parameters.items():
                parent_file_content.append(f'\t\tpath_parameters["{url_safe_string(param_schema["name"])}"] =  {param_name}\n')
            parent_file_content.append('\n')
        
        parent_file_content.append(f'\t\tfrom .{module_file_name_from_name(model_name)} import {module_class_name_from_name(model_name)}Request\n')
        
        if child_path_parameters:
            parent_file_content.append(f'\t\treturn {module_class_name_from_name(model_name)}Request(self.request_adapter, path_parameters)\n')
        else:
            parent_file_content.append(f'\t\treturn {module_class_name_from_name(model_name)}Request(self.request_adapter, self.path_parameters)\n')
        
        parent_file_content.append('\n')

    return parent_file_content

def add_missing_submodule_imports(paths:dict, components:dict):
    for path in paths.keys():



        path_parts = path.strip('/').split('/')

        for x in range(len(path_parts)-1):
            parent_name = path_parts[x]
            # parent_http_path = path[:path.rindex('/')]
            parent_http_path = '/'+ '/'.join(path_parts[:x+1])

            model_name:str = path_parts[x+1]
            child_http_path = '/'+ '/'.join(path_parts[:x+2])

            # Check if child model has a path parameter
            child_path_parameters = {}
            if child_http_path in paths.keys():
                child_path_parameters = paths[child_http_path].get('parameters', [])
                child_path_parameters: dict = resolve_path_parameters(child_path_parameters, components)
 

            parent_endpoint_path = os.path.join(client_generated_dir, *[module_file_name_from_name(part) for part in path_parts[:x+1]])
            parent_init_file = os.path.join(parent_endpoint_path, '__init__.py')
            parent_relative_path_to_root = '.' + '.'.join(['' for _ in range(len(path_parts[:x+1]))])

            # create the init file for endpoints that have no method, hence were not created in the previous step
            if not os.path.isfile(parent_init_file):
                write_init_file(
                    init_file_path=parent_init_file,
                    model_name = parent_name,
                    http_path = parent_http_path,
                    relative_path_to_root = parent_relative_path_to_root
                )


            with open(parent_init_file, 'r') as parent_init_file_obj:
                parent_file_content = parent_init_file_obj.readlines()

            # check if model is already defined as a property in the parent class
            if f'\tdef {module_file_name_from_name(model_name)}(self) -> {module_class_name_from_name(model_name)}Request:\n' in parent_file_content:
                continue

            else:
                parent_file_content = _child_in_parent_writes(parent_file_content, model_name, child_path_parameters)
                parent_file_content = (''.join(parent_file_content)).encode()
                with open(parent_init_file, 'w+b', buffering=0) as parent_init_file_obj:
                    parent_init_file_obj.write(parent_file_content)

def add_methods(paths:dict, components:dict):
    for path, methods in paths.items():

        # # ignore paths that have query param in path
        # if '(' in path:
        #     # print(f'Path {path} contains query parameters in path. Handling this not implemented yet...')
        #     continue

        # Create directory structure based on the path
        path_parts = path.strip('/').split('/')
        
        endpoint_path = os.path.join(client_generated_dir, *[module_file_name_from_name(part) for part in path_parts])
        endpoint_relative_path_to_root = '.' + '.'.join(['' for _ in range(len(path_parts))])
        
        # create folders for the collection and all submodules
        progressive_path = []
        for part in path_parts:
            progressive_path.append(module_file_name_from_name(part))
            file_path = os.path.join(client_generated_dir, *progressive_path)
            os.makedirs(file_path, exist_ok=True)

        # handle the methods
        method_dependencies = set()
        endpoint_method_funcs = []
        query_params = []

        for method, details in methods.items():
            path_parameters: list = methods.get('parameters', [])
            raw_path_param_keys = [param['name'] for param in resolve_path_parameters(path_parameters, components).values()]
            
            # Ensure details is a dictionary
            if not isinstance(details, dict):
                continue
            # Ensure methods are valid
            if method not in ['get', 'post', 'put', 'patch', 'delete']:
                continue

            endpoint_methods = _method_writes(
                method=method,
                details=details,
                endpoint_path=endpoint_path,
                path_parameters=path_parameters,
                http_path=path,
                components=components,
            )
            method_dependencies.update(endpoint_methods[0])
            endpoint_method_funcs.append(endpoint_methods[1])
            query_params.append(endpoint_methods[2])

        # write init file for the endpoint
        init_file_path = os.path.join(endpoint_path, '__init__.py')
        write_init_file(
            init_file_path=init_file_path, 
            model_name=path_parts[-1],
            http_path=path,
            relative_path_to_root=endpoint_relative_path_to_root,
            dependencies = method_dependencies,
            method_functions = endpoint_method_funcs,
            query_params = query_params,
            raw_path_param_keys = raw_path_param_keys,
        )

def add_generated_base_service_client(paths:dict):
    writes = []
    root_endpoints = set()
    base_service_client_file = os.path.join(client_generated_dir, '_generated_base_service_client.py')
    # iterate over the paths and only extract the first part of the path
    for path in paths.keys():
        path_parts = path.strip('/').split('/')
        model_name = path_parts[0]

        # # ignore paths that have query param in path
        # if '(' in model_name:
        #     print(f'Path {model_name} contains query parameters in path. Handling this not implemented yet...')
        #     continue

        root_endpoints.add(model_name)

    # write the imports
    writes.append('from __future__ import annotations\n')
    writes.append('from typing import TYPE_CHECKING\n')
    writes.append('\n')
    writes.append('if TYPE_CHECKING:\n')

    # write imports for the root endpoints
    for endpoint in root_endpoints:
        writes.append(f'\tfrom .{module_file_name_from_name(endpoint)} import {module_class_name_from_name(endpoint)}Request\n')
    writes.append('\n')
    writes.append('class GraphServiceClientBase:\n')
    writes.append('\n')
    for endpoint in root_endpoints:
        writes.append('\t@property\n')
        writes.append(f'\tdef {module_file_name_from_name(endpoint)}(self) -> {module_class_name_from_name(endpoint)}Request:\n')
        writes.append(f'\t\tfrom .{module_file_name_from_name(endpoint)} import {module_class_name_from_name(endpoint)}Request\n')
        writes.append(f'\t\treturn {module_class_name_from_name(endpoint)}Request(self.request_adapter, self.path_parameters)\n')
        writes.append('\n')
    writes.append('\n')

    with open(base_service_client_file, 'w+b') as base_service_client_file_obj:
        encoded_writes = ''.join(writes).encode()
        base_service_client_file_obj.write(encoded_writes)


def create_client_from_openapi(openapi_data):
    paths = openapi_data.get('paths')
    components = openapi_data.get('components')

    # remove and recreate the client_generated_dir
    if os.path.isdir(client_generated_dir):
        rmtree(client_generated_dir)
        os.makedirs(client_generated_dir, exist_ok=True)

    # create models from components
    add_methods(paths, components)

    # write_submodule_imports(paths)
    add_missing_submodule_imports(paths, components)

    # create the base service client
    add_generated_base_service_client(paths)

def create_models_from_openapi(openapi_data: dict):

    # remove and recreate the models_dir
    if os.path.isdir(models_dir):
        rmtree(models_dir)
        os.makedirs(models_dir, exist_ok=True)
    else:
        os.makedirs(models_dir, exist_ok=True)

    components = openapi_data.get('components', {})


    for name, schema in components.get('schemas', {}).items():
        create_model(name, schema, components)

def update_version_in_pyproject(version,pyproject_file):
    
    with open(pyproject_file, 'r') as file:
        pyproject_data = toml.load(file)
    
    pyproject_data['project']['version'] = version
    
    with open(pyproject_file, 'w') as file:
        toml.dump(pyproject_data, file)
    
    print(f"Version updated to {version} in {pyproject_file}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python update_version.py <new_version>")
        sys.exit(1)
    new_version = sys.argv[1]

    with open(openapi_file, 'r') as file:
        openapi_data = yaml.load(file,Loader=CoreLoader )

    create_models_from_openapi(openapi_data)
    create_client_from_openapi(openapi_data)

    client_pyproject_file = os.path.join(client_root_dir, 'pyproject.toml')
    models_pyproject_file = os.path.join(models_root_dir, 'pyproject.toml')

    update_version_in_pyproject(new_version, client_pyproject_file)
    update_version_in_pyproject(new_version, models_pyproject_file)
