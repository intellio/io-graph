from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows_updates_find_by_catalog_id_with_catalogidGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsUpdatesProduct]] = Field(alias="value", default=None,)

from .windows_updates_product import WindowsUpdatesProduct
