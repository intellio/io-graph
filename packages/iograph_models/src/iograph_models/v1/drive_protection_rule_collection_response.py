from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveProtectionRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DriveProtectionRule]] = Field(alias="value", default=None,)

from .drive_protection_rule import DriveProtectionRule
