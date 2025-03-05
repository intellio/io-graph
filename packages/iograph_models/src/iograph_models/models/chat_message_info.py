from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageInfo(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	body: Optional[ItemBody] = Field(default=None,alias="body",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	eventDetail: SerializeAsAny[Optional[EventMessageDetail]] = Field(default=None,alias="eventDetail",)
	from_: Optional[ChatMessageFromIdentitySet] = Field(default=None,alias="from",)
	isDeleted: Optional[bool] = Field(default=None,alias="isDeleted",)
	messageType: Optional[ChatMessageType] = Field(default=None,alias="messageType",)

from .item_body import ItemBody
from .event_message_detail import EventMessageDetail
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_type import ChatMessageType

