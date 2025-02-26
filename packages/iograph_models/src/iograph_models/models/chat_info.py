from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChatInfo(BaseModel):
	messageId: Optional[str] = Field(default=None,alias="messageId",)
	replyChainMessageId: Optional[str] = Field(default=None,alias="replyChainMessageId",)
	threadId: Optional[str] = Field(default=None,alias="threadId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


