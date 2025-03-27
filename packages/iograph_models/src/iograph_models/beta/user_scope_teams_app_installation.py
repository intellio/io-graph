from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UserScopeTeamsAppInstallation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userScopeTeamsAppInstallation"] = Field(alias="@odata.type", default="#microsoft.graph.userScopeTeamsAppInstallation")
	consentedPermissionSet: Optional[TeamsAppPermissionSet] = Field(alias="consentedPermissionSet", default=None,)
	scopeInfo: Optional[Union[GroupChatTeamsAppInstallationScopeInfo, PersonalTeamsAppInstallationScopeInfo, TeamTeamsAppInstallationScopeInfo]] = Field(alias="scopeInfo", default=None,discriminator="odata_type", )
	teamsApp: Optional[TeamsApp] = Field(alias="teamsApp", default=None,)
	teamsAppDefinition: Optional[TeamsAppDefinition] = Field(alias="teamsAppDefinition", default=None,)
	chat: Optional[Chat] = Field(alias="chat", default=None,)

from .teams_app_permission_set import TeamsAppPermissionSet
from .group_chat_teams_app_installation_scope_info import GroupChatTeamsAppInstallationScopeInfo
from .personal_teams_app_installation_scope_info import PersonalTeamsAppInstallationScopeInfo
from .team_teams_app_installation_scope_info import TeamTeamsAppInstallationScopeInfo
from .teams_app import TeamsApp
from .teams_app_definition import TeamsAppDefinition
from .chat import Chat

