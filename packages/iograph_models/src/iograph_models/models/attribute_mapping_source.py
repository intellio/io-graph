from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeMappingSource(BaseModel):
	expression: Optional[str] = Field(default=None,alias="expression",)
	name: Optional[str] = Field(default=None,alias="name",)
	parameters: Optional[list[StringKeyAttributeMappingSourceValuePair]] = Field(default=None,alias="parameters",)
	type: Optional[AttributeMappingSourceType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .string_key_attribute_mapping_source_value_pair import StringKeyAttributeMappingSourceValuePair
from .attribute_mapping_source_type import AttributeMappingSourceType

