from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Post(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	categories: list[Optional[str]] = Field(alias="categories",)
	changeKey: Optional[str] = Field(default=None,alias="changeKey",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	body: Optional[ItemBody] = Field(default=None,alias="body",)
	conversationId: Optional[str] = Field(default=None,alias="conversationId",)
	conversationThreadId: Optional[str] = Field(default=None,alias="conversationThreadId",)
	from_: Optional[Recipient] = Field(default=None,alias="from",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	newParticipants: list[Recipient] = Field(alias="newParticipants",)
	receivedDateTime: Optional[datetime] = Field(default=None,alias="receivedDateTime",)
	sender: Optional[Recipient] = Field(default=None,alias="sender",)
	attachments: list[Attachment] = Field(alias="attachments",)
	extensions: list[Extension] = Field(alias="extensions",)
	inReplyTo: Optional[Post] = Field(default=None,alias="inReplyTo",)
	multiValueExtendedProperties: list[MultiValueLegacyExtendedProperty] = Field(alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: list[SingleValueLegacyExtendedProperty] = Field(alias="singleValueExtendedProperties",)

from .item_body import ItemBody
from .recipient import Recipient
from .recipient import Recipient
from .recipient import Recipient
from .attachment import Attachment
from .extension import Extension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

