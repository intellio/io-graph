from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveProtectionUnitCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DriveProtectionUnit]] = Field(default=None,alias="value",)

from .drive_protection_unit import DriveProtectionUnit

