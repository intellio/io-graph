from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrivilegedAccess(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedAccess"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedAccess")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	resources: Optional[list[GovernanceResource]] = Field(alias="resources", default=None,)
	roleAssignmentRequests: Optional[list[GovernanceRoleAssignmentRequest]] = Field(alias="roleAssignmentRequests", default=None,)
	roleAssignments: Optional[list[GovernanceRoleAssignment]] = Field(alias="roleAssignments", default=None,)
	roleDefinitions: Optional[list[GovernanceRoleDefinition]] = Field(alias="roleDefinitions", default=None,)
	roleSettings: Optional[list[GovernanceRoleSetting]] = Field(alias="roleSettings", default=None,)

from .governance_resource import GovernanceResource
from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
from .governance_role_assignment import GovernanceRoleAssignment
from .governance_role_definition import GovernanceRoleDefinition
from .governance_role_setting import GovernanceRoleSetting
