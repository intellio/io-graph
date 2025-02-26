from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrivilegedAccessGroupAssignmentScheduleInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PrivilegedAccessGroupAssignmentScheduleInstance] = Field(alias="value",)

from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance

