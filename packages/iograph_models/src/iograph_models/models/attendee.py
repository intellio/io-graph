from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Attendee(BaseModel):
	emailAddress: Optional[EmailAddress] = Field(default=None,alias="emailAddress",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	type: Optional[AttendeeType] = Field(default=None,alias="type",)
	proposedNewTime: Optional[TimeSlot] = Field(default=None,alias="proposedNewTime",)
	status: Optional[ResponseStatus] = Field(default=None,alias="status",)

from .email_address import EmailAddress
from .attendee_type import AttendeeType
from .time_slot import TimeSlot
from .response_status import ResponseStatus

