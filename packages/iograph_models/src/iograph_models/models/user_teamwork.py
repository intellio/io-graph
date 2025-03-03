from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserTeamwork(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	locale: Optional[str] = Field(default=None,alias="locale",)
	region: Optional[str] = Field(default=None,alias="region",)
	associatedTeams: Optional[list[AssociatedTeamInfo]] = Field(default=None,alias="associatedTeams",)
	installedApps: Optional[list[UserScopeTeamsAppInstallation]] = Field(default=None,alias="installedApps",)

from .associated_team_info import AssociatedTeamInfo
from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

