from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ConversationThread(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	ccRecipients: Optional[list[Recipient]] = Field(default=None,alias="ccRecipients",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	isLocked: Optional[bool] = Field(default=None,alias="isLocked",)
	lastDeliveredDateTime: Optional[datetime] = Field(default=None,alias="lastDeliveredDateTime",)
	preview: Optional[str] = Field(default=None,alias="preview",)
	topic: Optional[str] = Field(default=None,alias="topic",)
	toRecipients: Optional[list[Recipient]] = Field(default=None,alias="toRecipients",)
	uniqueSenders: Optional[list[str]] = Field(default=None,alias="uniqueSenders",)
	posts: Optional[list[Post]] = Field(default=None,alias="posts",)

from .recipient import Recipient
from .recipient import Recipient
from .post import Post

