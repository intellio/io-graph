from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ObjectMappingMetadataEntry(BaseModel):
	key: Optional[ObjectMappingMetadata] = Field(default=None,alias="key",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .object_mapping_metadata import ObjectMappingMetadata

