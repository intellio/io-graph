from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosHomeScreenPageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosHomeScreenPage]] = Field(alias="value", default=None,)

from .ios_home_screen_page import IosHomeScreenPage
