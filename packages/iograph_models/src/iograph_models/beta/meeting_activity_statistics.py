from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingActivityStatistics(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	activity: Optional[AnalyticsActivityType | str] = Field(alias="activity",default=None,)
	duration: Optional[str] = Field(alias="duration",default=None,)
	endDate: Optional[str] = Field(alias="endDate",default=None,)
	startDate: Optional[str] = Field(alias="startDate",default=None,)
	timeZoneUsed: Optional[str] = Field(alias="timeZoneUsed",default=None,)
	afterHours: Optional[str] = Field(alias="afterHours",default=None,)
	conflicting: Optional[str] = Field(alias="conflicting",default=None,)
	long: Optional[str] = Field(alias="long",default=None,)
	multitasking: Optional[str] = Field(alias="multitasking",default=None,)
	organized: Optional[str] = Field(alias="organized",default=None,)
	recurring: Optional[str] = Field(alias="recurring",default=None,)

from .analytics_activity_type import AnalyticsActivityType

