from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RbacApplication(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	resourceNamespaces: Optional[list[UnifiedRbacResourceNamespace]] = Field(alias="resourceNamespaces", default=None,)
	roleAssignments: Optional[list[UnifiedRoleAssignment]] = Field(alias="roleAssignments", default=None,)
	roleAssignmentScheduleInstances: Optional[list[UnifiedRoleAssignmentScheduleInstance]] = Field(alias="roleAssignmentScheduleInstances", default=None,)
	roleAssignmentScheduleRequests: Optional[list[UnifiedRoleAssignmentScheduleRequest]] = Field(alias="roleAssignmentScheduleRequests", default=None,)
	roleAssignmentSchedules: Optional[list[UnifiedRoleAssignmentSchedule]] = Field(alias="roleAssignmentSchedules", default=None,)
	roleDefinitions: Optional[list[UnifiedRoleDefinition]] = Field(alias="roleDefinitions", default=None,)
	roleEligibilityScheduleInstances: Optional[list[UnifiedRoleEligibilityScheduleInstance]] = Field(alias="roleEligibilityScheduleInstances", default=None,)
	roleEligibilityScheduleRequests: Optional[list[UnifiedRoleEligibilityScheduleRequest]] = Field(alias="roleEligibilityScheduleRequests", default=None,)
	roleEligibilitySchedules: Optional[list[UnifiedRoleEligibilitySchedule]] = Field(alias="roleEligibilitySchedules", default=None,)

from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
from .unified_role_assignment import UnifiedRoleAssignment
from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

