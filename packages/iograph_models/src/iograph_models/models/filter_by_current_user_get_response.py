from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Filter_by_current_userGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[UnifiedRoleEligibilitySchedule]] = Field(default=None,alias="value",)

from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

