from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsQualityUpdateCatalogItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsQualityUpdateCatalogItem"] = Field(alias="@odata.type", default="#microsoft.graph.windowsQualityUpdateCatalogItem")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endOfSupportDate: Optional[datetime] = Field(alias="endOfSupportDate", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)
	classification: Optional[WindowsQualityUpdateCategory | str] = Field(alias="classification", default=None,)
	isExpeditable: Optional[bool] = Field(alias="isExpeditable", default=None,)
	kbArticleId: Optional[str] = Field(alias="kbArticleId", default=None,)
	productRevisions: Optional[list[WindowsQualityUpdateCatalogProductRevision]] = Field(alias="productRevisions", default=None,)
	qualityUpdateCadence: Optional[WindowsQualityUpdateCadence | str] = Field(alias="qualityUpdateCadence", default=None,)

from .windows_quality_update_category import WindowsQualityUpdateCategory
from .windows_quality_update_catalog_product_revision import WindowsQualityUpdateCatalogProductRevision
from .windows_quality_update_cadence import WindowsQualityUpdateCadence
