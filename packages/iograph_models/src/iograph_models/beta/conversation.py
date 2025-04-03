from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Conversation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.conversation"] = Field(alias="@odata.type", default="#microsoft.graph.conversation")
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	lastDeliveredDateTime: Optional[datetime] = Field(alias="lastDeliveredDateTime", default=None,)
	preview: Optional[str] = Field(alias="preview", default=None,)
	topic: Optional[str] = Field(alias="topic", default=None,)
	uniqueSenders: Optional[list[str]] = Field(alias="uniqueSenders", default=None,)
	threads: Optional[list[ConversationThread]] = Field(alias="threads", default=None,)

from .conversation_thread import ConversationThread
