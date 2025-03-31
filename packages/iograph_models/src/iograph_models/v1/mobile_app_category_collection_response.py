from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileAppCategoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MobileAppCategory]] = Field(alias="value", default=None,)

from .mobile_app_category import MobileAppCategory
