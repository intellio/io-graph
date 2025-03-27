from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UserScopeTeamsAppInstallation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userScopeTeamsAppInstallation"] = Field(alias="@odata.type", default="#microsoft.graph.userScopeTeamsAppInstallation")
	consentedPermissionSet: Optional[TeamsAppPermissionSet] = Field(alias="consentedPermissionSet", default=None,)
	teamsApp: Optional[TeamsApp] = Field(alias="teamsApp", default=None,)
	teamsAppDefinition: Optional[TeamsAppDefinition] = Field(alias="teamsAppDefinition", default=None,)
	chat: Optional[Chat] = Field(alias="chat", default=None,)

from .teams_app_permission_set import TeamsAppPermissionSet
from .teams_app import TeamsApp
from .teams_app_definition import TeamsAppDefinition
from .chat import Chat

