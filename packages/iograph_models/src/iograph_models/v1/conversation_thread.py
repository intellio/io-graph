from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class ConversationThread(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.conversationThread"] = Field(alias="@odata.type",)
	ccRecipients: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="ccRecipients", default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	isLocked: Optional[bool] = Field(alias="isLocked", default=None,)
	lastDeliveredDateTime: Optional[datetime] = Field(alias="lastDeliveredDateTime", default=None,)
	preview: Optional[str] = Field(alias="preview", default=None,)
	topic: Optional[str] = Field(alias="topic", default=None,)
	toRecipients: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="toRecipients", default=None,)
	uniqueSenders: Optional[list[str]] = Field(alias="uniqueSenders", default=None,)
	posts: Optional[list[Post]] = Field(alias="posts", default=None,)

from .attendee import Attendee
from .post import Post
