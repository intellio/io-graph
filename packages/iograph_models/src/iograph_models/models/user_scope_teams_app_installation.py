from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserScopeTeamsAppInstallation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	consentedPermissionSet: Optional[TeamsAppPermissionSet] = Field(default=None,alias="consentedPermissionSet",)
	teamsApp: Optional[TeamsApp] = Field(default=None,alias="teamsApp",)
	teamsAppDefinition: Optional[TeamsAppDefinition] = Field(default=None,alias="teamsAppDefinition",)
	chat: Optional[Chat] = Field(default=None,alias="chat",)

from .teams_app_permission_set import TeamsAppPermissionSet
from .teams_app import TeamsApp
from .teams_app_definition import TeamsAppDefinition
from .chat import Chat

