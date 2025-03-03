from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RbacApplication(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	resourceNamespaces: Optional[list[UnifiedRbacResourceNamespace]] = Field(default=None,alias="resourceNamespaces",)
	roleAssignments: Optional[list[UnifiedRoleAssignment]] = Field(default=None,alias="roleAssignments",)
	roleAssignmentScheduleInstances: Optional[list[UnifiedRoleAssignmentScheduleInstance]] = Field(default=None,alias="roleAssignmentScheduleInstances",)
	roleAssignmentScheduleRequests: Optional[list[UnifiedRoleAssignmentScheduleRequest]] = Field(default=None,alias="roleAssignmentScheduleRequests",)
	roleAssignmentSchedules: Optional[list[UnifiedRoleAssignmentSchedule]] = Field(default=None,alias="roleAssignmentSchedules",)
	roleDefinitions: Optional[list[UnifiedRoleDefinition]] = Field(default=None,alias="roleDefinitions",)
	roleEligibilityScheduleInstances: Optional[list[UnifiedRoleEligibilityScheduleInstance]] = Field(default=None,alias="roleEligibilityScheduleInstances",)
	roleEligibilityScheduleRequests: Optional[list[UnifiedRoleEligibilityScheduleRequest]] = Field(default=None,alias="roleEligibilityScheduleRequests",)
	roleEligibilitySchedules: Optional[list[UnifiedRoleEligibilitySchedule]] = Field(default=None,alias="roleEligibilitySchedules",)

from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
from .unified_role_assignment import UnifiedRoleAssignment
from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

