from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesApplicableContent(BaseModel):
	catalogEntryId: Optional[str] = Field(alias="catalogEntryId",default=None,)
	catalogEntry: SerializeAsAny[Optional[WindowsUpdatesCatalogEntry]] = Field(alias="catalogEntry",default=None,)
	matchedDevices: Optional[list[WindowsUpdatesApplicableContentDeviceMatch]] = Field(alias="matchedDevices",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows_updates_catalog_entry import WindowsUpdatesCatalogEntry
from .windows_updates_applicable_content_device_match import WindowsUpdatesApplicableContentDeviceMatch

