from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserTeamwork(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	region: Optional[str] = Field(alias="region", default=None,)
	associatedTeams: Optional[list[AssociatedTeamInfo]] = Field(alias="associatedTeams", default=None,)
	installedApps: Optional[list[UserScopeTeamsAppInstallation]] = Field(alias="installedApps", default=None,)

from .associated_team_info import AssociatedTeamInfo
from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

