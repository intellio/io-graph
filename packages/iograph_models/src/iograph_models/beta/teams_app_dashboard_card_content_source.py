from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppDashboardCardContentSource(BaseModel):
	botConfiguration: Optional[TeamsAppDashboardCardBotConfiguration] = Field(alias="botConfiguration", default=None,)
	sourceType: Optional[TeamsAppDashboardCardSourceType | str] = Field(alias="sourceType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teams_app_dashboard_card_bot_configuration import TeamsAppDashboardCardBotConfiguration
from .teams_app_dashboard_card_source_type import TeamsAppDashboardCardSourceType
