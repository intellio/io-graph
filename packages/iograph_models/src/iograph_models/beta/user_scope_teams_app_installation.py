from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserScopeTeamsAppInstallation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	consentedPermissionSet: Optional[TeamsAppPermissionSet] = Field(alias="consentedPermissionSet",default=None,)
	scopeInfo: SerializeAsAny[Optional[TeamsAppInstallationScopeInfo]] = Field(alias="scopeInfo",default=None,)
	teamsApp: Optional[TeamsApp] = Field(alias="teamsApp",default=None,)
	teamsAppDefinition: Optional[TeamsAppDefinition] = Field(alias="teamsAppDefinition",default=None,)
	chat: Optional[Chat] = Field(alias="chat",default=None,)

from .teams_app_permission_set import TeamsAppPermissionSet
from .teams_app_installation_scope_info import TeamsAppInstallationScopeInfo
from .teams_app import TeamsApp
from .teams_app_definition import TeamsAppDefinition
from .chat import Chat

