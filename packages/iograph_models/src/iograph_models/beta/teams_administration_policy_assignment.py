from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAdministrationPolicyAssignment(BaseModel):
	assignmentType: Optional[TeamsAdministrationAssignmentType | str] = Field(alias="assignmentType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	groupId: Optional[str] = Field(alias="groupId",default=None,)
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teams_administration_assignment_type import TeamsAdministrationAssignmentType

