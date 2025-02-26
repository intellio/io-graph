from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleAssignmentScheduleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UnifiedRoleAssignmentSchedule] = Field(alias="value",)

from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule

