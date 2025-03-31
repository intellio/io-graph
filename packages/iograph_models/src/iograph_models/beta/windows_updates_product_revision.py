from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdatesProductRevision(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.productRevision"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isHotpatchUpdate: Optional[bool] = Field(alias="isHotpatchUpdate", default=None,)
	osBuild: Optional[WindowsUpdatesBuildVersionDetails] = Field(alias="osBuild", default=None,)
	product: Optional[str] = Field(alias="product", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	catalogEntry: Optional[Union[WindowsUpdatesDriverUpdateCatalogEntry, WindowsUpdatesFeatureUpdateCatalogEntry, WindowsUpdatesQualityUpdateCatalogEntry]] = Field(alias="catalogEntry", default=None,discriminator="odata_type", )
	knowledgeBaseArticle: Optional[WindowsUpdatesKnowledgeBaseArticle] = Field(alias="knowledgeBaseArticle", default=None,)

from .windows_updates_build_version_details import WindowsUpdatesBuildVersionDetails
from .windows_updates_driver_update_catalog_entry import WindowsUpdatesDriverUpdateCatalogEntry
from .windows_updates_feature_update_catalog_entry import WindowsUpdatesFeatureUpdateCatalogEntry
from .windows_updates_quality_update_catalog_entry import WindowsUpdatesQualityUpdateCatalogEntry
from .windows_updates_knowledge_base_article import WindowsUpdatesKnowledgeBaseArticle
