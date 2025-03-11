from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingReminder(BaseModel):
	message: Optional[str] = Field(alias="message",default=None,)
	offset: Optional[str] = Field(alias="offset",default=None,)
	recipients: Optional[BookingReminderRecipients | str] = Field(alias="recipients",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .booking_reminder_recipients import BookingReminderRecipients

