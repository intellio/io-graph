from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AutomaticRepliesMailTips(BaseModel):
	message: Optional[str] = Field(alias="message",default=None,)
	messageLanguage: Optional[LocaleInfo] = Field(alias="messageLanguage",default=None,)
	scheduledEndTime: Optional[DateTimeTimeZone] = Field(alias="scheduledEndTime",default=None,)
	scheduledStartTime: Optional[DateTimeTimeZone] = Field(alias="scheduledStartTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .locale_info import LocaleInfo
from .date_time_time_zone import DateTimeTimeZone
from .date_time_time_zone import DateTimeTimeZone

