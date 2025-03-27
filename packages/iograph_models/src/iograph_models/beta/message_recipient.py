from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MessageRecipient(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deliveryStatus: Optional[MessageStatus | str] = Field(alias="deliveryStatus", default=None,)
	recipientEmail: Optional[str] = Field(alias="recipientEmail", default=None,)
	events: Optional[list[MessageEvent]] = Field(alias="events", default=None,)

from .message_status import MessageStatus
from .message_event import MessageEvent

