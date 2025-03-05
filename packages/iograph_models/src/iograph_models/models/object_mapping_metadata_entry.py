from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ObjectMappingMetadataEntry(BaseModel):
	key: Optional[str | ObjectMappingMetadata] = Field(alias="key",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .object_mapping_metadata import ObjectMappingMetadata

