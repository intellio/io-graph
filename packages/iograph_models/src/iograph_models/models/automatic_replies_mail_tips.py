from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AutomaticRepliesMailTips(BaseModel):
	message: Optional[str] = Field(default=None,alias="message",)
	messageLanguage: Optional[LocaleInfo] = Field(default=None,alias="messageLanguage",)
	scheduledEndTime: Optional[DateTimeTimeZone] = Field(default=None,alias="scheduledEndTime",)
	scheduledStartTime: Optional[DateTimeTimeZone] = Field(default=None,alias="scheduledStartTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .locale_info import LocaleInfo
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

