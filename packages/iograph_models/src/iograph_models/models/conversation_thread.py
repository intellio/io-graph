from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ConversationThread(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	ccRecipients: list[Recipient] = Field(alias="ccRecipients",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	isLocked: Optional[bool] = Field(default=None,alias="isLocked",)
	lastDeliveredDateTime: Optional[datetime] = Field(default=None,alias="lastDeliveredDateTime",)
	preview: Optional[str] = Field(default=None,alias="preview",)
	topic: Optional[str] = Field(default=None,alias="topic",)
	toRecipients: list[Recipient] = Field(alias="toRecipients",)
	uniqueSenders: list[str] = Field(alias="uniqueSenders",)
	posts: list[Post] = Field(alias="posts",)

from .recipient import Recipient
from .recipient import Recipient
from .post import Post

