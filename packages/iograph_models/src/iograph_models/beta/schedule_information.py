from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ScheduleInformation(BaseModel):
	availabilityView: Optional[str] = Field(alias="availabilityView",default=None,)
	error: Optional[FreeBusyError] = Field(alias="error",default=None,)
	scheduleId: Optional[str] = Field(alias="scheduleId",default=None,)
	scheduleItems: Optional[list[ScheduleItem]] = Field(alias="scheduleItems",default=None,)
	workingHours: Optional[WorkingHours] = Field(alias="workingHours",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .free_busy_error import FreeBusyError
from .schedule_item import ScheduleItem
from .working_hours import WorkingHours

