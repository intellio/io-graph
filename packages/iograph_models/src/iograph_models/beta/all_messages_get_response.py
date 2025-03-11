from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class All_messagesGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ChatMessage]] = Field(alias="value",default=None,)

from .chat_message import ChatMessage

