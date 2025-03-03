from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleAssignmentScheduleInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[UnifiedRoleAssignmentScheduleInstance]] = Field(default=None,alias="value",)

from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance

