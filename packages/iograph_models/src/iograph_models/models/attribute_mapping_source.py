from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeMappingSource(BaseModel):
	expression: Optional[str] = Field(alias="expression",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	parameters: Optional[list[StringKeyAttributeMappingSourceValuePair]] = Field(alias="parameters",default=None,)
	type: Optional[str | AttributeMappingSourceType] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .string_key_attribute_mapping_source_value_pair import StringKeyAttributeMappingSourceValuePair
from .attribute_mapping_source_type import AttributeMappingSourceType

