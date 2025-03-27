from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MessageEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	dateTime: Optional[datetime] = Field(alias="dateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	eventType: Optional[MessageEventType | str] = Field(alias="eventType", default=None,)

from .message_event_type import MessageEventType

