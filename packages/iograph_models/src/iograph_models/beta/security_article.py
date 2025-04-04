from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityArticle(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.article"] = Field(alias="@odata.type", default="#microsoft.graph.security.article")
	body: Optional[SecurityFormattedContent] = Field(alias="body", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	imageUrl: Optional[str] = Field(alias="imageUrl", default=None,)
	isFeatured: Optional[bool] = Field(alias="isFeatured", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	summary: Optional[SecurityFormattedContent] = Field(alias="summary", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	indicators: Optional[list[SecurityArticleIndicator]] = Field(alias="indicators", default=None,)

from .security_formatted_content import SecurityFormattedContent
from .security_article_indicator import SecurityArticleIndicator
