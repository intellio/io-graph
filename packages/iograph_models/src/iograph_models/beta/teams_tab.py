from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamsTab(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	configuration: Optional[TeamsTabConfiguration] = Field(alias="configuration",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	messageId: Optional[str] = Field(alias="messageId",default=None,)
	sortOrderIndex: Optional[str] = Field(alias="sortOrderIndex",default=None,)
	teamsAppId: Optional[str] = Field(alias="teamsAppId",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	teamsApp: Optional[TeamsApp] = Field(alias="teamsApp",default=None,)

from .teams_tab_configuration import TeamsTabConfiguration
from .teams_app import TeamsApp

