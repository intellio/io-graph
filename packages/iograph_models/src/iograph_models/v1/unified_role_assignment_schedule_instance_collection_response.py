from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleAssignmentScheduleInstanceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UnifiedRoleAssignmentScheduleInstance]] = Field(alias="value", default=None,)

from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance

