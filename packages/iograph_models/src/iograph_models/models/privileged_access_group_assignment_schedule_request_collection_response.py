from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrivilegedAccessGroupAssignmentScheduleRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[PrivilegedAccessGroupAssignmentScheduleRequest]] = Field(default=None,alias="value",)

from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest

