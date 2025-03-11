from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerTaskRecurrence(BaseModel):
	nextInSeriesTaskId: Optional[str] = Field(alias="nextInSeriesTaskId",default=None,)
	occurrenceId: Optional[int] = Field(alias="occurrenceId",default=None,)
	previousInSeriesTaskId: Optional[str] = Field(alias="previousInSeriesTaskId",default=None,)
	recurrenceStartDateTime: Optional[datetime] = Field(alias="recurrenceStartDateTime",default=None,)
	schedule: Optional[PlannerRecurrenceSchedule] = Field(alias="schedule",default=None,)
	seriesId: Optional[str] = Field(alias="seriesId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .planner_recurrence_schedule import PlannerRecurrenceSchedule

