from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TimeConstraint(BaseModel):
	activityDomain: Optional[ActivityDomain | str] = Field(alias="activityDomain", default=None,)
	timeSlots: Optional[list[TimeSlot]] = Field(alias="timeSlots", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .activity_domain import ActivityDomain
from .time_slot import TimeSlot

