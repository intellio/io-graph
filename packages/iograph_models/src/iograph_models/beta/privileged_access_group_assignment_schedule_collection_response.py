from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrivilegedAccessGroupAssignmentScheduleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PrivilegedAccessGroupAssignmentSchedule]] = Field(alias="value", default=None,)

from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
