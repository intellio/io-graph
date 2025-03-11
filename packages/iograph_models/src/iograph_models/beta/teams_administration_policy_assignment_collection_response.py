from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAdministrationPolicyAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[TeamsAdministrationPolicyAssignment]] = Field(alias="value",default=None,)

from .teams_administration_policy_assignment import TeamsAdministrationPolicyAssignment

