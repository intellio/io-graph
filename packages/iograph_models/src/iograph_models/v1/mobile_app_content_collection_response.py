from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileAppContentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MobileAppContent]] = Field(alias="value", default=None,)

from .mobile_app_content import MobileAppContent
