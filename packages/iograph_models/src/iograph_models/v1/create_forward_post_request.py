from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class Create_forwardPostRequest(BaseModel):
	ToRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee],Field(discriminator="odata_type")]]] = Field(alias="ToRecipients", default=None,)
	Message: Optional[Union[CalendarSharingMessage, EventMessage, EventMessageRequest, EventMessageResponse]] = Field(alias="Message", default=None,discriminator="odata_type", )
	Comment: Optional[str] = Field(alias="Comment", default=None,)

from .attendee_base import AttendeeBase
from .attendee import Attendee
from .calendar_sharing_message import CalendarSharingMessage
from .event_message import EventMessage
from .event_message_request import EventMessageRequest
from .event_message_response import EventMessageResponse

