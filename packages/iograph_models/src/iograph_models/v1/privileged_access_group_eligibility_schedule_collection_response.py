from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrivilegedAccessGroupEligibilityScheduleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PrivilegedAccessGroupEligibilitySchedule]] = Field(alias="value", default=None,)

from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
