from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class MessageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[CalendarSharingMessage, EventMessageRequest, EventMessageResponse],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .calendar_sharing_message import CalendarSharingMessage
from .event_message_request import EventMessageRequest
from .event_message_response import EventMessageResponse
