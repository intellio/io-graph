from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAppDashboardCardBotConfiguration(BaseModel):
	botId: Optional[str] = Field(alias="botId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

