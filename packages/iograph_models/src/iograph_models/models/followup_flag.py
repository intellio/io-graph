from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FollowupFlag(BaseModel):
	completedDateTime: Optional[DateTimeTimeZone] = Field(alias="completedDateTime",default=None,)
	dueDateTime: Optional[DateTimeTimeZone] = Field(alias="dueDateTime",default=None,)
	flagStatus: Optional[FollowupFlagStatus | str] = Field(alias="flagStatus",default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone
from .followup_flag_status import FollowupFlagStatus
from .date_time_time_zone import DateTimeTimeZone

