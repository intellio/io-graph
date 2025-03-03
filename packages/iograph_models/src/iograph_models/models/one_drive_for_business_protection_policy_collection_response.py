from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OneDriveForBusinessProtectionPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OneDriveForBusinessProtectionPolicy]] = Field(default=None,alias="value",)

from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy

