from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Send_virtual_appointment_smsPostRequest(BaseModel):
	messageType: Optional[VirtualAppointmentMessageType] = Field(default=None,alias="messageType",)
	attendees: Optional[list[AttendeeNotificationInfo]] = Field(default=None,alias="attendees",)

from .virtual_appointment_message_type import VirtualAppointmentMessageType
from .attendee_notification_info import AttendeeNotificationInfo

