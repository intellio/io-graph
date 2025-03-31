from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Send_virtual_appointment_smsPostRequest(BaseModel):
	messageType: Optional[VirtualAppointmentMessageType | str] = Field(alias="messageType", default=None,)
	attendees: Optional[list[AttendeeNotificationInfo]] = Field(alias="attendees", default=None,)

from .virtual_appointment_message_type import VirtualAppointmentMessageType
from .attendee_notification_info import AttendeeNotificationInfo
