from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ItemAttachment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.itemAttachment"] = Field(alias="@odata.type", default="#microsoft.graph.itemAttachment")
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	isInline: Optional[bool] = Field(alias="isInline", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	item: Optional[Union[Contact, Event, MailboxItem, CalendarSharingMessage, EventMessageRequest, EventMessageResponse, Note, OutlookTask, Post]] = Field(alias="item", default=None,discriminator="odata_type", )

from .contact import Contact
from .event import Event
from .mailbox_item import MailboxItem
from .calendar_sharing_message import CalendarSharingMessage
from .event_message_request import EventMessageRequest
from .event_message_response import EventMessageResponse
from .note import Note
from .outlook_task import OutlookTask
from .post import Post
