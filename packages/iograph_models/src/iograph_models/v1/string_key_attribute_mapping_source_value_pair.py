from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StringKeyAttributeMappingSourceValuePair(BaseModel):
	key: Optional[str] = Field(alias="key",default=None,)
	value: Optional[AttributeMappingSource] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attribute_mapping_source import AttributeMappingSource

