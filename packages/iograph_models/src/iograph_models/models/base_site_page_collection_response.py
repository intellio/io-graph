from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BaseSitePageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[BaseSitePage] = Field(alias="value",)

from .base_site_page import BaseSitePage

