from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesSoftwareUpdateCatalogEntryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[WindowsUpdatesSoftwareUpdateCatalogEntry]]] = Field(alias="value",default=None,)

from .windows_updates_software_update_catalog_entry import WindowsUpdatesSoftwareUpdateCatalogEntry

