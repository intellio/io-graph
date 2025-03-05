from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StringKeyAttributeMappingSourceValuePair(BaseModel):
	key: Optional[str] = Field(default=None,alias="key",)
	value: Optional[AttributeMappingSource] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attribute_mapping_source import AttributeMappingSource

