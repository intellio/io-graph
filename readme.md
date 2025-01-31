## Generate Openapi file
To generate openapi that only contains the required components run:

```
python autogen.py
```

Note that list of components that are required are set in the script

## Generate Pydantic models
to generte pydantic models from local file:  
```
datamodel-codegen --input ./openapi.yaml --input-file-type openapi --output ./src/iograph --output-model-type pydantic_v2.BaseModel --use-annotated --use-union-operator --snake-case-field --no-alias    
```
to generte pydantic models from url: 
```
datamodel-codegen --url https://github.com/microsoftgraph/msgraph-metadata/raw/refs/heads/master/openapi/v1.0/openapi.yaml --input-file-type openapi --output ./src/iograph --output-model-type pydantic_v2.BaseModel --use-annotated --use-union-operator --snake-case-field --no-alias    
```
## Post process

1. inside graph.__init__.py, move any line that imports from graph folder to bottom of file just 
   before where model_rebuilds are defined
2. in other files inside graph folder, fix the relative imports
3. One post-generation task is to remove patterns from datetime fields in generated models as it 
causes issues until we find a proper solution

## Build package
run this command to create the python package:
```
python3 -m build
```

Package will be ready under dist/ folder