from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignmentApprovals: Optional[list[Approval]] = Field(default=None,alias="assignmentApprovals",)
	assignmentScheduleInstances: Optional[list[PrivilegedAccessGroupAssignmentScheduleInstance]] = Field(default=None,alias="assignmentScheduleInstances",)
	assignmentScheduleRequests: Optional[list[PrivilegedAccessGroupAssignmentScheduleRequest]] = Field(default=None,alias="assignmentScheduleRequests",)
	assignmentSchedules: Optional[list[PrivilegedAccessGroupAssignmentSchedule]] = Field(default=None,alias="assignmentSchedules",)
	eligibilityScheduleInstances: Optional[list[PrivilegedAccessGroupEligibilityScheduleInstance]] = Field(default=None,alias="eligibilityScheduleInstances",)
	eligibilityScheduleRequests: Optional[list[PrivilegedAccessGroupEligibilityScheduleRequest]] = Field(default=None,alias="eligibilityScheduleRequests",)
	eligibilitySchedules: Optional[list[PrivilegedAccessGroupEligibilitySchedule]] = Field(default=None,alias="eligibilitySchedules",)

from .approval import Approval
from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

