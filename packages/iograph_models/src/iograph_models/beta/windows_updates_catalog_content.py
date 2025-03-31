from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class WindowsUpdatesCatalogContent(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsUpdates.catalogContent"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.catalogContent")
	catalogEntry: Optional[Union[WindowsUpdatesDriverUpdateCatalogEntry, WindowsUpdatesFeatureUpdateCatalogEntry, WindowsUpdatesQualityUpdateCatalogEntry]] = Field(alias="catalogEntry", default=None,discriminator="odata_type", )

from .windows_updates_driver_update_catalog_entry import WindowsUpdatesDriverUpdateCatalogEntry
from .windows_updates_feature_update_catalog_entry import WindowsUpdatesFeatureUpdateCatalogEntry
from .windows_updates_quality_update_catalog_entry import WindowsUpdatesQualityUpdateCatalogEntry
