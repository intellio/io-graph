from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleEligibilityScheduleInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UnifiedRoleEligibilityScheduleInstance]] = Field(alias="value", default=None,)

from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
