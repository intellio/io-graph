from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class Post(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.post"] = Field(alias="@odata.type", default="#microsoft.graph.post")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	conversationId: Optional[str] = Field(alias="conversationId", default=None,)
	conversationThreadId: Optional[str] = Field(alias="conversationThreadId", default=None,)
	from_: Optional[Union[Attendee]] = Field(alias="from", default=None,discriminator="odata_type", )
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	importance: Optional[Importance | str] = Field(alias="importance", default=None,)
	newParticipants: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="newParticipants", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	sender: Optional[Union[Attendee]] = Field(alias="sender", default=None,discriminator="odata_type", )
	attachments: Optional[list[Annotated[Union[FileAttachment, ItemAttachment, ReferenceAttachment],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension, PersonExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	inReplyTo: Optional[Post] = Field(alias="inReplyTo", default=None,)
	mentions: Optional[list[Mention]] = Field(alias="mentions", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .item_body import ItemBody
from .attendee import Attendee
from .importance import Importance
from .file_attachment import FileAttachment
from .item_attachment import ItemAttachment
from .reference_attachment import ReferenceAttachment
from .open_type_extension import OpenTypeExtension
from .person_extension import PersonExtension
from .mention import Mention
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
