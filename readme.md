## Generate Openapi file
To generate openapi that only contains the required components run:

```
python autogen.py
```

Note that list of components that are required are set in the script

If you choose to go this path, then we can only generate the models from local file as explained below

## Generate Pydantic models
to generte pydantic models from local file:  
```
datamodel-codegen --input ./openapi.yaml --input-file-type openapi --output ./src/iograph --output-model-type pydantic_v2.BaseModel --snake-case-field --no-alias --target-python-version 3.13 --use-standard-collections  --use-union-operator
```
to generte pydantic models from url: 
```
datamodel-codegen --url https://github.com/microsoftgraph/msgraph-metadata/raw/refs/heads/master/openapi/v1.0/openapi.yaml --input-file-type openapi --output ./src/iograph --output-model-type pydantic_v2.BaseModel --snake-case-field --no-alias --target-python-version 3.13 --use-standard-collections --field-constraints --use-union-operator 
```
## Post process

1. in all files fix the relative imports
2. remove all model_rebuild() calls from all files. rebuilds cause issue with ForwardRef annotations
   and Pydantic has builting mechanisms to handle it. https://docs.pydantic.dev/latest/internals/resolving_annotations/
3. in microsoft.graph._init__ move models that are imported in other files before the import statements.
   for instance, class Entity is imported by multiple other files, so we should move it before any 
   relative import in __init__ file.
4. One post-generation task is to remove patterns from datetime fields in generated models as it 
   causes issues until we find a proper solution. use this regular expression to find all of them 
   ^.*(pattern=).*\n?
5. remove Dict[str, Any] or dict[str, Any] from all models where it is part of a union e.g SomeModel | Dict[str, Any] | None
   the reason for this is that msgspec doesn't allow it. more info https://jcristharif.com/msgspec/supported-types.html#union-optional

## Build package
run this command to create the python package:
```
python3 -m build
```

Package will be ready under dist/ folder

