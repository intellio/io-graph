from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Send_virtual_appointment_reminder_smsPostRequest(BaseModel):
	remindBeforeTimeInMinutesType: Optional[RemindBeforeTimeInMinutesType | str] = Field(alias="remindBeforeTimeInMinutesType",default=None,)
	attendees: Optional[list[AttendeeNotificationInfo]] = Field(alias="attendees",default=None,)

from .remind_before_time_in_minutes_type import RemindBeforeTimeInMinutesType
from .attendee_notification_info import AttendeeNotificationInfo

