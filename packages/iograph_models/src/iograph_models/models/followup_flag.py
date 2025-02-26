from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class FollowupFlag(BaseModel):
	completedDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="completedDateTime",)
	dueDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="dueDateTime",)
	flagStatus: Optional[FollowupFlagStatus] = Field(default=None,alias="flagStatus",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .followup_flag_status import FollowupFlagStatus
from .date_time_time_zone import DateTimeTimeZone

