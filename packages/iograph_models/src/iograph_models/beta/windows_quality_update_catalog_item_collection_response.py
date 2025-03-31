from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsQualityUpdateCatalogItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsQualityUpdateCatalogItem]] = Field(alias="value", default=None,)

from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem
