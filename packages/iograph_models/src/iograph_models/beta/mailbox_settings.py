from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MailboxSettings(BaseModel):
	archiveFolder: Optional[str] = Field(alias="archiveFolder", default=None,)
	automaticRepliesSetting: Optional[AutomaticRepliesSetting] = Field(alias="automaticRepliesSetting", default=None,)
	dateFormat: Optional[str] = Field(alias="dateFormat", default=None,)
	delegateMeetingMessageDeliveryOptions: Optional[DelegateMeetingMessageDeliveryOptions | str] = Field(alias="delegateMeetingMessageDeliveryOptions", default=None,)
	language: Optional[LocaleInfo] = Field(alias="language", default=None,)
	timeFormat: Optional[str] = Field(alias="timeFormat", default=None,)
	timeZone: Optional[str] = Field(alias="timeZone", default=None,)
	userPurpose: Optional[UserPurpose | str] = Field(alias="userPurpose", default=None,)
	userPurposeV2: Optional[MailboxRecipientType | str] = Field(alias="userPurposeV2", default=None,)
	workingHours: Optional[WorkingHours] = Field(alias="workingHours", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .automatic_replies_setting import AutomaticRepliesSetting
from .delegate_meeting_message_delivery_options import DelegateMeetingMessageDeliveryOptions
from .locale_info import LocaleInfo
from .user_purpose import UserPurpose
from .mailbox_recipient_type import MailboxRecipientType
from .working_hours import WorkingHours

