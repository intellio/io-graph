from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RolesAssignedOutsidePrivilegedIdentityManagementAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident"] = Field(alias="@odata.type", default="#microsoft.graph.rolesAssignedOutsidePrivilegedIdentityManagementAlertIncident")
	assigneeDisplayName: Optional[str] = Field(alias="assigneeDisplayName", default=None,)
	assigneeId: Optional[str] = Field(alias="assigneeId", default=None,)
	assigneeUserPrincipalName: Optional[str] = Field(alias="assigneeUserPrincipalName", default=None,)
	assignmentCreatedDateTime: Optional[datetime] = Field(alias="assignmentCreatedDateTime", default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	roleDisplayName: Optional[str] = Field(alias="roleDisplayName", default=None,)
	roleTemplateId: Optional[str] = Field(alias="roleTemplateId", default=None,)


