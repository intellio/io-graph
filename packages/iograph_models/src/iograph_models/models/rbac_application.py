from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RbacApplication(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	resourceNamespaces: list[UnifiedRbacResourceNamespace] = Field(alias="resourceNamespaces",)
	roleAssignments: list[UnifiedRoleAssignment] = Field(alias="roleAssignments",)
	roleAssignmentScheduleInstances: list[UnifiedRoleAssignmentScheduleInstance] = Field(alias="roleAssignmentScheduleInstances",)
	roleAssignmentScheduleRequests: list[UnifiedRoleAssignmentScheduleRequest] = Field(alias="roleAssignmentScheduleRequests",)
	roleAssignmentSchedules: list[UnifiedRoleAssignmentSchedule] = Field(alias="roleAssignmentSchedules",)
	roleDefinitions: list[UnifiedRoleDefinition] = Field(alias="roleDefinitions",)
	roleEligibilityScheduleInstances: list[UnifiedRoleEligibilityScheduleInstance] = Field(alias="roleEligibilityScheduleInstances",)
	roleEligibilityScheduleRequests: list[UnifiedRoleEligibilityScheduleRequest] = Field(alias="roleEligibilityScheduleRequests",)
	roleEligibilitySchedules: list[UnifiedRoleEligibilitySchedule] = Field(alias="roleEligibilitySchedules",)

from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
from .unified_role_assignment import UnifiedRoleAssignment
from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
from .unified_role_definition import UnifiedRoleDefinition
from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

