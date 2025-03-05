from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationMetadataEntryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SynchronizationMetadataEntry]] = Field(alias="value",default=None,)

from .synchronization_metadata_entry import SynchronizationMetadataEntry

