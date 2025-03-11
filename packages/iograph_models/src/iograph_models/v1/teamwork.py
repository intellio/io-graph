from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Teamwork(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isTeamsEnabled: Optional[bool] = Field(alias="isTeamsEnabled",default=None,)
	region: Optional[str] = Field(alias="region",default=None,)
	deletedChats: Optional[list[DeletedChat]] = Field(alias="deletedChats",default=None,)
	deletedTeams: Optional[list[DeletedTeam]] = Field(alias="deletedTeams",default=None,)
	teamsAppSettings: Optional[TeamsAppSettings] = Field(alias="teamsAppSettings",default=None,)
	workforceIntegrations: Optional[list[WorkforceIntegration]] = Field(alias="workforceIntegrations",default=None,)

from .deleted_chat import DeletedChat
from .deleted_team import DeletedTeam
from .teams_app_settings import TeamsAppSettings
from .workforce_integration import WorkforceIntegration

