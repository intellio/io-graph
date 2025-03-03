from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Teamwork(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isTeamsEnabled: Optional[bool] = Field(default=None,alias="isTeamsEnabled",)
	region: Optional[str] = Field(default=None,alias="region",)
	deletedChats: Optional[list[DeletedChat]] = Field(default=None,alias="deletedChats",)
	deletedTeams: Optional[list[DeletedTeam]] = Field(default=None,alias="deletedTeams",)
	teamsAppSettings: Optional[TeamsAppSettings] = Field(default=None,alias="teamsAppSettings",)
	workforceIntegrations: Optional[list[WorkforceIntegration]] = Field(default=None,alias="workforceIntegrations",)

from .deleted_chat import DeletedChat
from .deleted_team import DeletedTeam
from .teams_app_settings import TeamsAppSettings
from .workforce_integration import WorkforceIntegration

