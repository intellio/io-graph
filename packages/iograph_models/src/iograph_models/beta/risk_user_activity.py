from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RiskUserActivity(BaseModel):
	detail: Optional[RiskDetail | str] = Field(alias="detail", default=None,)
	eventTypes: Optional[list[RiskEventType | str]] = Field(alias="eventTypes", default=None,)
	riskEventTypes: Optional[list[str]] = Field(alias="riskEventTypes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .risk_detail import RiskDetail
from .risk_event_type import RiskEventType
