from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsQualityUpdateCatalogProductRevision(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	knowledgeBaseArticle: Optional[WindowsQualityUpdateProductKnowledgeBaseArticle] = Field(alias="knowledgeBaseArticle", default=None,)
	osBuild: Optional[WindowsQualityUpdateProductBuildVersionDetail] = Field(alias="osBuild", default=None,)
	productName: Optional[str] = Field(alias="productName", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)
	versionName: Optional[str] = Field(alias="versionName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_quality_update_product_knowledge_base_article import WindowsQualityUpdateProductKnowledgeBaseArticle
from .windows_quality_update_product_build_version_detail import WindowsQualityUpdateProductBuildVersionDetail
