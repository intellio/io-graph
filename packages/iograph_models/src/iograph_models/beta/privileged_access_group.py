from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegedAccessGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	assignmentApprovals: Optional[list[Approval]] = Field(alias="assignmentApprovals", default=None,)
	assignmentScheduleInstances: Optional[list[PrivilegedAccessGroupAssignmentScheduleInstance]] = Field(alias="assignmentScheduleInstances", default=None,)
	assignmentScheduleRequests: Optional[list[PrivilegedAccessGroupAssignmentScheduleRequest]] = Field(alias="assignmentScheduleRequests", default=None,)
	assignmentSchedules: Optional[list[PrivilegedAccessGroupAssignmentSchedule]] = Field(alias="assignmentSchedules", default=None,)
	eligibilityScheduleInstances: Optional[list[PrivilegedAccessGroupEligibilityScheduleInstance]] = Field(alias="eligibilityScheduleInstances", default=None,)
	eligibilityScheduleRequests: Optional[list[PrivilegedAccessGroupEligibilityScheduleRequest]] = Field(alias="eligibilityScheduleRequests", default=None,)
	eligibilitySchedules: Optional[list[PrivilegedAccessGroupEligibilitySchedule]] = Field(alias="eligibilitySchedules", default=None,)

from .approval import Approval
from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

