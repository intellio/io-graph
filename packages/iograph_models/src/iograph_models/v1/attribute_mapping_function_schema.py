from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AttributeMappingFunctionSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.attributeMappingFunctionSchema"] = Field(alias="@odata.type", default="#microsoft.graph.attributeMappingFunctionSchema")
	parameters: Optional[list[AttributeMappingParameterSchema]] = Field(alias="parameters", default=None,)

from .attribute_mapping_parameter_schema import AttributeMappingParameterSchema
