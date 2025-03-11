from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Post(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	changeKey: Optional[str] = Field(alias="changeKey",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	body: Optional[ItemBody] = Field(alias="body",default=None,)
	conversationId: Optional[str] = Field(alias="conversationId",default=None,)
	conversationThreadId: Optional[str] = Field(alias="conversationThreadId",default=None,)
	from_: SerializeAsAny[Optional[Recipient]] = Field(alias="from",default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments",default=None,)
	importance: Optional[Importance | str] = Field(alias="importance",default=None,)
	newParticipants: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="newParticipants",default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime",default=None,)
	sender: SerializeAsAny[Optional[Recipient]] = Field(alias="sender",default=None,)
	attachments: SerializeAsAny[Optional[list[Attachment]]] = Field(alias="attachments",default=None,)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(alias="extensions",default=None,)
	inReplyTo: Optional[Post] = Field(alias="inReplyTo",default=None,)
	mentions: Optional[list[Mention]] = Field(alias="mentions",default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties",default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties",default=None,)

from .item_body import ItemBody
from .recipient import Recipient
from .importance import Importance
from .recipient import Recipient
from .recipient import Recipient
from .attachment import Attachment
from .extension import Extension
from .mention import Mention
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

