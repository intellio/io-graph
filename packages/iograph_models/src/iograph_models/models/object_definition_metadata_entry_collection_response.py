from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ObjectDefinitionMetadataEntryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ObjectDefinitionMetadataEntry]] = Field(default=None,alias="value",)

from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

