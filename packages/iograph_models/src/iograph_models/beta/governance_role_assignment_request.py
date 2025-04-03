from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GovernanceRoleAssignmentRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.governanceRoleAssignmentRequest"] = Field(alias="@odata.type", default="#microsoft.graph.governanceRoleAssignmentRequest")
	assignmentState: Optional[str] = Field(alias="assignmentState", default=None,)
	linkedEligibleRoleAssignmentId: Optional[str] = Field(alias="linkedEligibleRoleAssignmentId", default=None,)
	reason: Optional[str] = Field(alias="reason", default=None,)
	requestedDateTime: Optional[datetime] = Field(alias="requestedDateTime", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	schedule: Optional[GovernanceSchedule] = Field(alias="schedule", default=None,)
	status: Optional[GovernanceRoleAssignmentRequestStatus] = Field(alias="status", default=None,)
	subjectId: Optional[str] = Field(alias="subjectId", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	resource: Optional[GovernanceResource] = Field(alias="resource", default=None,)
	roleDefinition: Optional[GovernanceRoleDefinition] = Field(alias="roleDefinition", default=None,)
	subject: Optional[GovernanceSubject] = Field(alias="subject", default=None,)

from .governance_schedule import GovernanceSchedule
from .governance_role_assignment_request_status import GovernanceRoleAssignmentRequestStatus
from .governance_resource import GovernanceResource
from .governance_role_definition import GovernanceRoleDefinition
from .governance_subject import GovernanceSubject
