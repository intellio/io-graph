from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttributeDefinitionMetadataEntryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AttributeDefinitionMetadataEntry] = Field(alias="value",)

from .attribute_definition_metadata_entry import AttributeDefinitionMetadataEntry

