from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsTab(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	configuration: Optional[TeamsTabConfiguration] = Field(default=None,alias="configuration",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	teamsApp: Optional[TeamsApp] = Field(default=None,alias="teamsApp",)

from .teams_tab_configuration import TeamsTabConfiguration
from .teams_app import TeamsApp

