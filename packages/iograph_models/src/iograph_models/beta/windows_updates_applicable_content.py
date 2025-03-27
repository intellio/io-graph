from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesApplicableContent(BaseModel):
	catalogEntryId: Optional[str] = Field(alias="catalogEntryId", default=None,)
	catalogEntry: Optional[Union[WindowsUpdatesSoftwareUpdateCatalogEntry, WindowsUpdatesDriverUpdateCatalogEntry, WindowsUpdatesFeatureUpdateCatalogEntry, WindowsUpdatesQualityUpdateCatalogEntry]] = Field(alias="catalogEntry", default=None,discriminator="odata_type", )
	matchedDevices: Optional[list[WindowsUpdatesApplicableContentDeviceMatch]] = Field(alias="matchedDevices", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_software_update_catalog_entry import WindowsUpdatesSoftwareUpdateCatalogEntry
from .windows_updates_driver_update_catalog_entry import WindowsUpdatesDriverUpdateCatalogEntry
from .windows_updates_feature_update_catalog_entry import WindowsUpdatesFeatureUpdateCatalogEntry
from .windows_updates_quality_update_catalog_entry import WindowsUpdatesQualityUpdateCatalogEntry
from .windows_updates_applicable_content_device_match import WindowsUpdatesApplicableContentDeviceMatch

