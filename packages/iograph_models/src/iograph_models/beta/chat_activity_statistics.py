from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ChatActivityStatistics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.chatActivityStatistics"] = Field(alias="@odata.type", default="#microsoft.graph.chatActivityStatistics")
	activity: Optional[AnalyticsActivityType | str] = Field(alias="activity", default=None,)
	duration: Optional[str] = Field(alias="duration", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	timeZoneUsed: Optional[str] = Field(alias="timeZoneUsed", default=None,)
	afterHours: Optional[str] = Field(alias="afterHours", default=None,)

from .analytics_activity_type import AnalyticsActivityType
