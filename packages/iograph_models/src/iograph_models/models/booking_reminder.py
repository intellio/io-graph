from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BookingReminder(BaseModel):
	message: Optional[str] = Field(default=None,alias="message",)
	offset: Optional[str] = Field(default=None,alias="offset",)
	recipients: Optional[BookingReminderRecipients] = Field(default=None,alias="recipients",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .booking_reminder_recipients import BookingReminderRecipients

