from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamsTab(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsTab"] = Field(alias="@odata.type",)
	configuration: Optional[TeamsTabConfiguration] = Field(alias="configuration", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	teamsApp: Optional[TeamsApp] = Field(alias="teamsApp", default=None,)

from .teams_tab_configuration import TeamsTabConfiguration
from .teams_app import TeamsApp
