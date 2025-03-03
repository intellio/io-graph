from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Conversation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	lastDeliveredDateTime: Optional[datetime] = Field(default=None,alias="lastDeliveredDateTime",)
	preview: Optional[str] = Field(default=None,alias="preview",)
	topic: Optional[str] = Field(default=None,alias="topic",)
	uniqueSenders: Optional[list[str]] = Field(default=None,alias="uniqueSenders",)
	threads: Optional[list[ConversationThread]] = Field(default=None,alias="threads",)

from .conversation_thread import ConversationThread

