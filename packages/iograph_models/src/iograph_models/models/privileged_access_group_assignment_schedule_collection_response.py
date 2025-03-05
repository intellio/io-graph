from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroupAssignmentScheduleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[PrivilegedAccessGroupAssignmentSchedule]] = Field(default=None,alias="value",)

from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule

