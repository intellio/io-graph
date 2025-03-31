from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ComanagementEligibleDevicesSummary(BaseModel):
	comanagedCount: Optional[int] = Field(alias="comanagedCount", default=None,)
	eligibleButNotAzureAdJoinedCount: Optional[int] = Field(alias="eligibleButNotAzureAdJoinedCount", default=None,)
	eligibleCount: Optional[int] = Field(alias="eligibleCount", default=None,)
	ineligibleCount: Optional[int] = Field(alias="ineligibleCount", default=None,)
	needsOsUpdateCount: Optional[int] = Field(alias="needsOsUpdateCount", default=None,)
	scheduledForEnrollmentCount: Optional[int] = Field(alias="scheduledForEnrollmentCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

