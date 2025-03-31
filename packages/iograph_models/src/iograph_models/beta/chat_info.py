from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatInfo(BaseModel):
	messageId: Optional[str] = Field(alias="messageId", default=None,)
	replyChainMessageId: Optional[str] = Field(alias="replyChainMessageId", default=None,)
	threadId: Optional[str] = Field(alias="threadId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

