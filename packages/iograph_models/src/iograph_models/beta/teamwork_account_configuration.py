from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkAccountConfiguration(BaseModel):
	onPremisesCalendarSyncConfiguration: Optional[TeamworkOnPremisesCalendarSyncConfiguration] = Field(alias="onPremisesCalendarSyncConfiguration", default=None,)
	supportedClient: Optional[TeamworkSupportedClient | str] = Field(alias="supportedClient", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_on_premises_calendar_sync_configuration import TeamworkOnPremisesCalendarSyncConfiguration
from .teamwork_supported_client import TeamworkSupportedClient
