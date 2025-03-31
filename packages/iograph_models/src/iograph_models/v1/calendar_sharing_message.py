from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class CalendarSharingMessage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.calendarSharingMessage"] = Field(alias="@odata.type", default="#microsoft.graph.calendarSharingMessage")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	bccRecipients: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="bccRecipients", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	bodyPreview: Optional[str] = Field(alias="bodyPreview", default=None,)
	ccRecipients: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="ccRecipients", default=None,)
	conversationId: Optional[str] = Field(alias="conversationId", default=None,)
	conversationIndex: Optional[str] = Field(alias="conversationIndex", default=None,)
	flag: Optional[FollowupFlag] = Field(alias="flag", default=None,)
	from_: Optional[Union[Attendee]] = Field(alias="from", default=None,discriminator="odata_type", )
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	importance: Optional[Importance | str] = Field(alias="importance", default=None,)
	inferenceClassification: Optional[InferenceClassificationType | str] = Field(alias="inferenceClassification", default=None,)
	internetMessageHeaders: Optional[list[InternetMessageHeader]] = Field(alias="internetMessageHeaders", default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId", default=None,)
	isDeliveryReceiptRequested: Optional[bool] = Field(alias="isDeliveryReceiptRequested", default=None,)
	isDraft: Optional[bool] = Field(alias="isDraft", default=None,)
	isRead: Optional[bool] = Field(alias="isRead", default=None,)
	isReadReceiptRequested: Optional[bool] = Field(alias="isReadReceiptRequested", default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	replyTo: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="replyTo", default=None,)
	sender: Optional[Union[Attendee]] = Field(alias="sender", default=None,discriminator="odata_type", )
	sentDateTime: Optional[datetime] = Field(alias="sentDateTime", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	toRecipients: Optional[list[Annotated[Union[Attendee],Field(discriminator="odata_type")]]] = Field(alias="toRecipients", default=None,)
	uniqueBody: Optional[ItemBody] = Field(alias="uniqueBody", default=None,)
	webLink: Optional[str] = Field(alias="webLink", default=None,)
	attachments: Optional[list[Annotated[Union[FileAttachment, ItemAttachment, ReferenceAttachment],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)
	canAccept: Optional[bool] = Field(alias="canAccept", default=None,)
	sharingMessageAction: Optional[CalendarSharingMessageAction] = Field(alias="sharingMessageAction", default=None,)
	sharingMessageActions: Optional[list[CalendarSharingMessageAction]] = Field(alias="sharingMessageActions", default=None,)
	suggestedCalendarName: Optional[str] = Field(alias="suggestedCalendarName", default=None,)

from .attendee import Attendee
from .item_body import ItemBody
from .followup_flag import FollowupFlag
from .importance import Importance
from .inference_classification_type import InferenceClassificationType
from .internet_message_header import InternetMessageHeader
from .file_attachment import FileAttachment
from .item_attachment import ItemAttachment
from .reference_attachment import ReferenceAttachment
from .open_type_extension import OpenTypeExtension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from .calendar_sharing_message_action import CalendarSharingMessageAction
