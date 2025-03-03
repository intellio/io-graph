from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttributeMappingFunctionSchema(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	parameters: Optional[list[AttributeMappingParameterSchema]] = Field(default=None,alias="parameters",)

from .attribute_mapping_parameter_schema import AttributeMappingParameterSchema

