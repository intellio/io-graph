from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveProtectionRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DriveProtectionRule] = Field(alias="value",)

from .drive_protection_rule import DriveProtectionRule

