from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeMappingFunctionSchema(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	parameters: Optional[list[AttributeMappingParameterSchema]] = Field(alias="parameters",default=None,)

from .attribute_mapping_parameter_schema import AttributeMappingParameterSchema

