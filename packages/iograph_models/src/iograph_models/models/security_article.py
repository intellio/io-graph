from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityArticle(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	body: Optional[SecurityFormattedContent] = Field(default=None,alias="body",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	imageUrl: Optional[str] = Field(default=None,alias="imageUrl",)
	isFeatured: Optional[bool] = Field(default=None,alias="isFeatured",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	summary: Optional[SecurityFormattedContent] = Field(default=None,alias="summary",)
	tags: list[Optional[str]] = Field(alias="tags",)
	title: Optional[str] = Field(default=None,alias="title",)
	indicators: list[SecurityArticleIndicator] = Field(alias="indicators",)

from .security_formatted_content import SecurityFormattedContent
from .security_formatted_content import SecurityFormattedContent
from .security_article_indicator import SecurityArticleIndicator

