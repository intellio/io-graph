from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Send_virtual_appointment_reminder_smsPostRequest(BaseModel):
	remindBeforeTimeInMinutesType: Optional[RemindBeforeTimeInMinutesType] = Field(default=None,alias="remindBeforeTimeInMinutesType",)
	attendees: Optional[list[AttendeeNotificationInfo]] = Field(default=None,alias="attendees",)

from .remind_before_time_in_minutes_type import RemindBeforeTimeInMinutesType
from .attendee_notification_info import AttendeeNotificationInfo

