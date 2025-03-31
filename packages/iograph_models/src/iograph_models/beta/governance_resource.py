from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GovernanceResource(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.governanceResource"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	registeredDateTime: Optional[datetime] = Field(alias="registeredDateTime", default=None,)
	registeredRoot: Optional[str] = Field(alias="registeredRoot", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	parent: Optional[GovernanceResource] = Field(alias="parent", default=None,)
	roleAssignmentRequests: Optional[list[GovernanceRoleAssignmentRequest]] = Field(alias="roleAssignmentRequests", default=None,)
	roleAssignments: Optional[list[GovernanceRoleAssignment]] = Field(alias="roleAssignments", default=None,)
	roleDefinitions: Optional[list[GovernanceRoleDefinition]] = Field(alias="roleDefinitions", default=None,)
	roleSettings: Optional[list[GovernanceRoleSetting]] = Field(alias="roleSettings", default=None,)

from .governance_role_assignment_request import GovernanceRoleAssignmentRequest
from .governance_role_assignment import GovernanceRoleAssignment
from .governance_role_definition import GovernanceRoleDefinition
from .governance_role_setting import GovernanceRoleSetting
