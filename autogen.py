import yaml


def extract_component_references(component_name, components, visited, new_components):
    if component_name in visited:
        return
    visited.add(component_name)
    
    component = components.get(component_name)
    if not component:
        return
    
    # Add the component to the new components dictionary
    new_components[component_name] = component
    
    # Recursively extract references from the component's properties
    def process_component(prop):
        if '$ref' in prop:
            ref_name = prop['$ref'].split('/')[-1]
            extract_component_references(ref_name, components, visited, new_components)
        elif 'items' in prop and '$ref' in prop['items']:
            ref_name = prop['items']['$ref'].split('/')[-1]
            extract_component_references(ref_name, components, visited, new_components)
        elif 'items' in prop and 'allOf' in prop['items']:
            for item in prop['items']['allOf']:
                process_component(item)
        elif 'items' in prop and 'anyOf' in prop['items']:
            for item in prop['items']['anyOf']:
                process_component(item)
        elif 'items' in prop and 'oneOf' in prop['items']:
            for item in prop['items']['oneOf']:
                process_component(item)
        elif 'allOf' in prop:
            for item in prop['allOf']:
                process_component(item)
        elif 'anyOf' in prop:
            for item in prop['anyOf']:
                process_component(item)
        elif 'oneOf' in prop:
            for item in prop['oneOf']:
                process_component(item)

    if 'properties' in component:
        for prop in component['properties'].values():
            process_component(prop)
    if 'allOf' in component:
        for item in component['allOf']:
            if 'properties' in item:
                for prop in item['properties'].values():
                    process_component(prop)
            else:
                process_component(item)
    if 'anyOf' in component:
        for item in component['anyOf']:
            if 'properties' in item:
                for prop in item['properties'].values():
                    process_component(prop)
            else:
                process_component(item)
    if 'oneOf' in component:
        for item in component['oneOf']:
            if 'properties' in item:
                for prop in item['properties'].values():
                    process_component(prop)
            else:
                process_component(item)

def generate_new_openapi_file(input_file, output_file, required_components):
    with open(input_file, 'r') as f:
        openapi_data = yaml.safe_load(f)
    
    components = openapi_data.get('components', {}).get('schemas', {})
    new_components = {}
    visited = set()
    
    for required_component in required_components:
        extract_component_references(required_component, components, visited, new_components)
    
    new_openapi_data = {
        'openapi': openapi_data['openapi'],
        'info': openapi_data['info'],
        'servers': openapi_data['servers'],
        'paths': {},
        'components': {
            'schemas': {}
        },
        'tags': openapi_data['tags']
    }
    new_openapi_data['components']['schemas'] = new_components
    
    with open(output_file, 'w') as f:
        yaml.safe_dump(new_openapi_data, f, default_flow_style=False)

# Example usage
input_file = 'openapi-full.yaml'
output_file = 'new_openapi.yaml'
required_component = [
    'microsoft.graph.user',
    'microsoft.graph.group',
    'microsoft.graph.conditionalAccessPolicy',
    'microsoft.graph.countryNamedLocation',
    'microsoft.graph.ipNamedLocation',
    'microsoft.graph.unifiedRoleDefinition',
    'microsoft.graph.tenantInformation',
    'microsoft.graph.authenticationContextClassReference',

    
    
    ]
generate_new_openapi_file(input_file, output_file, required_component)