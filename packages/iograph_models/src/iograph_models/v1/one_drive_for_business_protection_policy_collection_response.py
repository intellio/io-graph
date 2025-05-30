from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OneDriveForBusinessProtectionPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OneDriveForBusinessProtectionPolicy]] = Field(alias="value", default=None,)

from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
