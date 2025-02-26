from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SiteProtectionUnitCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SiteProtectionUnit] = Field(alias="value",)

from .site_protection_unit import SiteProtectionUnit

