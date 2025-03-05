from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupEligibilityScheduleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[PrivilegedAccessGroupEligibilitySchedule]] = Field(default=None,alias="value",)

from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

