from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessageInfo(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	body: Optional[ItemBody] = Field(alias="body",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	eventDetail: SerializeAsAny[Optional[EventMessageDetail]] = Field(alias="eventDetail",default=None,)
	from_: Optional[ChatMessageFromIdentitySet] = Field(alias="from",default=None,)
	isDeleted: Optional[bool] = Field(alias="isDeleted",default=None,)
	messageType: Optional[ChatMessageType | str] = Field(alias="messageType",default=None,)

from .item_body import ItemBody
from .event_message_detail import EventMessageDetail
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_type import ChatMessageType

