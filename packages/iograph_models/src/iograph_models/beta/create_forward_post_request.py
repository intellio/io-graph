from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class Create_forwardPostRequest(BaseModel):
	ToRecipients: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="ToRecipients", default=None,)
	Message: Optional[Union[CalendarSharingMessage, EventMessageRequest, EventMessageResponse]] = Field(alias="Message", default=None,discriminator="odata_type", )
	Comment: Optional[str] = Field(alias="Comment", default=None,)

from .attendee import Attendee
from .calendar_sharing_message import CalendarSharingMessage
from .event_message_request import EventMessageRequest
from .event_message_response import EventMessageResponse
