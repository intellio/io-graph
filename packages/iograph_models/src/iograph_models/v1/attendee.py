from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class Attendee(BaseModel):
	emailAddress: Optional[EmailAddress] = Field(alias="emailAddress", default=None,)
	odata_type: Literal["#microsoft.graph.attendee"] = Field(alias="@odata.type", default="#microsoft.graph.attendee")
	type: Optional[AttendeeType | str] = Field(alias="type", default=None,)
	proposedNewTime: Optional[TimeSlot] = Field(alias="proposedNewTime", default=None,)
	status: Optional[ResponseStatus] = Field(alias="status", default=None,)

from .email_address import EmailAddress
from .attendee_type import AttendeeType
from .time_slot import TimeSlot
from .response_status import ResponseStatus

