from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ScheduleInformation(BaseModel):
	availabilityView: Optional[str] = Field(default=None,alias="availabilityView",)
	error: Optional[FreeBusyError] = Field(default=None,alias="error",)
	scheduleId: Optional[str] = Field(default=None,alias="scheduleId",)
	scheduleItems: Optional[list[ScheduleItem]] = Field(default=None,alias="scheduleItems",)
	workingHours: Optional[WorkingHours] = Field(default=None,alias="workingHours",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .free_busy_error import FreeBusyError
from .schedule_item import ScheduleItem
from .working_hours import WorkingHours

