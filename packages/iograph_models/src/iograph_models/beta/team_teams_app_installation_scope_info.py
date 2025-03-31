from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamTeamsAppInstallationScopeInfo(BaseModel):
	scope: Optional[TeamsAppInstallationScopes | str] = Field(alias="scope", default=None,)
	odata_type: Literal["#microsoft.graph.teamTeamsAppInstallationScopeInfo"] = Field(alias="@odata.type", default="#microsoft.graph.teamTeamsAppInstallationScopeInfo")
	teamId: Optional[str] = Field(alias="teamId", default=None,)

from .teams_app_installation_scopes import TeamsAppInstallationScopes
