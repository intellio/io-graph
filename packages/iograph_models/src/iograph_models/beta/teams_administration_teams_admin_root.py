from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsAdministrationTeamsAdminRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	policy: Optional[TeamsAdministrationTeamsPolicyAssignment] = Field(alias="policy",default=None,)

from .teams_administration_teams_policy_assignment import TeamsAdministrationTeamsPolicyAssignment

