from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamsAdministrationTeamsPolicyAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsAdministration.teamsPolicyAssignment"] = Field(alias="@odata.type",)

