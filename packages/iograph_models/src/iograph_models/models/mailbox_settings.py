from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MailboxSettings(BaseModel):
	archiveFolder: Optional[str] = Field(default=None,alias="archiveFolder",)
	automaticRepliesSetting: Optional[AutomaticRepliesSetting] = Field(default=None,alias="automaticRepliesSetting",)
	dateFormat: Optional[str] = Field(default=None,alias="dateFormat",)
	delegateMeetingMessageDeliveryOptions: Optional[DelegateMeetingMessageDeliveryOptions] = Field(default=None,alias="delegateMeetingMessageDeliveryOptions",)
	language: Optional[LocaleInfo] = Field(default=None,alias="language",)
	timeFormat: Optional[str] = Field(default=None,alias="timeFormat",)
	timeZone: Optional[str] = Field(default=None,alias="timeZone",)
	userPurpose: Optional[UserPurpose] = Field(default=None,alias="userPurpose",)
	workingHours: Optional[WorkingHours] = Field(default=None,alias="workingHours",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .automatic_replies_setting import AutomaticRepliesSetting
from .delegate_meeting_message_delivery_options import DelegateMeetingMessageDeliveryOptions
from .locale_info import LocaleInfo
from .user_purpose import UserPurpose
from .working_hours import WorkingHours

