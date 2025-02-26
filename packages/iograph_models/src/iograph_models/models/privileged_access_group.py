from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrivilegedAccessGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignmentApprovals: list[Approval] = Field(alias="assignmentApprovals",)
	assignmentScheduleInstances: list[PrivilegedAccessGroupAssignmentScheduleInstance] = Field(alias="assignmentScheduleInstances",)
	assignmentScheduleRequests: list[PrivilegedAccessGroupAssignmentScheduleRequest] = Field(alias="assignmentScheduleRequests",)
	assignmentSchedules: list[PrivilegedAccessGroupAssignmentSchedule] = Field(alias="assignmentSchedules",)
	eligibilityScheduleInstances: list[PrivilegedAccessGroupEligibilityScheduleInstance] = Field(alias="eligibilityScheduleInstances",)
	eligibilityScheduleRequests: list[PrivilegedAccessGroupEligibilityScheduleRequest] = Field(alias="eligibilityScheduleRequests",)
	eligibilitySchedules: list[PrivilegedAccessGroupEligibilitySchedule] = Field(alias="eligibilitySchedules",)

from .approval import Approval
from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

