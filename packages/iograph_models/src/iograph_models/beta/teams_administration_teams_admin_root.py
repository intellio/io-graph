from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamsAdministrationTeamsAdminRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsAdministration.teamsAdminRoot"] = Field(alias="@odata.type",)
	policy: Optional[TeamsAdministrationTeamsPolicyAssignment] = Field(alias="policy", default=None,)

from .teams_administration_teams_policy_assignment import TeamsAdministrationTeamsPolicyAssignment
