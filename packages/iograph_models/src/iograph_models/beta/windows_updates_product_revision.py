from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesProductRevision(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isHotpatchUpdate: Optional[bool] = Field(alias="isHotpatchUpdate",default=None,)
	osBuild: Optional[WindowsUpdatesBuildVersionDetails] = Field(alias="osBuild",default=None,)
	product: Optional[str] = Field(alias="product",default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	catalogEntry: SerializeAsAny[Optional[WindowsUpdatesCatalogEntry]] = Field(alias="catalogEntry",default=None,)
	knowledgeBaseArticle: Optional[WindowsUpdatesKnowledgeBaseArticle] = Field(alias="knowledgeBaseArticle",default=None,)

from .windows_updates_build_version_details import WindowsUpdatesBuildVersionDetails
from .windows_updates_catalog_entry import WindowsUpdatesCatalogEntry
from .windows_updates_knowledge_base_article import WindowsUpdatesKnowledgeBaseArticle

