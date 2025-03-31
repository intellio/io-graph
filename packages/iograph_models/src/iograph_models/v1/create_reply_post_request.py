from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class Create_replyPostRequest(BaseModel):
	Message: Optional[Union[CalendarSharingMessage, EventMessageRequest, EventMessageResponse]] = Field(alias="Message", default=None,discriminator="odata_type", )
	Comment: Optional[str] = Field(alias="Comment", default=None,)

from .calendar_sharing_message import CalendarSharingMessage
from .event_message_request import EventMessageRequest
from .event_message_response import EventMessageResponse
