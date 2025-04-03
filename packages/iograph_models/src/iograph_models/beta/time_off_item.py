from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TimeOffItem(BaseModel):
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	theme: Optional[ScheduleEntityTheme | str] = Field(alias="theme", default=None,)
	odata_type: Literal["#microsoft.graph.timeOffItem"] = Field(alias="@odata.type", default="#microsoft.graph.timeOffItem")
	timeOffReasonId: Optional[str] = Field(alias="timeOffReasonId", default=None,)

from .schedule_entity_theme import ScheduleEntityTheme
