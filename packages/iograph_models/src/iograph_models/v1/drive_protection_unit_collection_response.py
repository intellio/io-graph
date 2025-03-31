from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveProtectionUnitCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DriveProtectionUnit]] = Field(alias="value", default=None,)

from .drive_protection_unit import DriveProtectionUnit
