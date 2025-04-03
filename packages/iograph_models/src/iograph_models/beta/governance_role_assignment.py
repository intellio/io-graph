from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GovernanceRoleAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.governanceRoleAssignment"] = Field(alias="@odata.type", default="#microsoft.graph.governanceRoleAssignment")
	assignmentState: Optional[str] = Field(alias="assignmentState", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	linkedEligibleRoleAssignmentId: Optional[str] = Field(alias="linkedEligibleRoleAssignmentId", default=None,)
	memberType: Optional[str] = Field(alias="memberType", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	subjectId: Optional[str] = Field(alias="subjectId", default=None,)
	linkedEligibleRoleAssignment: Optional[GovernanceRoleAssignment] = Field(alias="linkedEligibleRoleAssignment", default=None,)
	resource: Optional[GovernanceResource] = Field(alias="resource", default=None,)
	roleDefinition: Optional[GovernanceRoleDefinition] = Field(alias="roleDefinition", default=None,)
	subject: Optional[GovernanceSubject] = Field(alias="subject", default=None,)

from .governance_resource import GovernanceResource
from .governance_role_definition import GovernanceRoleDefinition
from .governance_subject import GovernanceSubject
