from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityArticleIndicatorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityArticleIndicator]] = Field(alias="value", default=None,)

from .security_article_indicator import SecurityArticleIndicator
