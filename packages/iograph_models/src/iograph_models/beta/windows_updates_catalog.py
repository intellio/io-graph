from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class WindowsUpdatesCatalog(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.catalog"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.catalog")
	entries: Optional[list[Annotated[Union[WindowsUpdatesDriverUpdateCatalogEntry, WindowsUpdatesFeatureUpdateCatalogEntry, WindowsUpdatesQualityUpdateCatalogEntry],Field(discriminator="odata_type")]]] = Field(alias="entries", default=None,)

from .windows_updates_driver_update_catalog_entry import WindowsUpdatesDriverUpdateCatalogEntry
from .windows_updates_feature_update_catalog_entry import WindowsUpdatesFeatureUpdateCatalogEntry
from .windows_updates_quality_update_catalog_entry import WindowsUpdatesQualityUpdateCatalogEntry
