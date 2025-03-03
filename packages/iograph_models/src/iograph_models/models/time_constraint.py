from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TimeConstraint(BaseModel):
	activityDomain: Optional[ActivityDomain] = Field(default=None,alias="activityDomain",)
	timeSlots: Optional[list[TimeSlot]] = Field(default=None,alias="timeSlots",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .activity_domain import ActivityDomain
from .time_slot import TimeSlot

