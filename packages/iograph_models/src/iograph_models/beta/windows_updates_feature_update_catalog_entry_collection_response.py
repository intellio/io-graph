from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdatesFeatureUpdateCatalogEntryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsUpdatesFeatureUpdateCatalogEntry]] = Field(alias="value", default=None,)

from .windows_updates_feature_update_catalog_entry import WindowsUpdatesFeatureUpdateCatalogEntry
