from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationMetadataEntryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SynchronizationMetadataEntry] = Field(alias="value",)

from .synchronization_metadata_entry import SynchronizationMetadataEntry

