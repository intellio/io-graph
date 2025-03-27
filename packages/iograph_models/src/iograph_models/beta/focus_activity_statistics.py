from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class FocusActivityStatistics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.focusActivityStatistics"] = Field(alias="@odata.type", default="#microsoft.graph.focusActivityStatistics")
	activity: Optional[AnalyticsActivityType | str] = Field(alias="activity", default=None,)
	duration: Optional[str] = Field(alias="duration", default=None,)
	endDate: Optional[str] = Field(alias="endDate", default=None,)
	startDate: Optional[str] = Field(alias="startDate", default=None,)
	timeZoneUsed: Optional[str] = Field(alias="timeZoneUsed", default=None,)

from .analytics_activity_type import AnalyticsActivityType

