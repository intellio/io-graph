from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CalendarSharingMessage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	categories: Optional[list[str]] = Field(default=None,alias="categories",)
	changeKey: Optional[str] = Field(default=None,alias="changeKey",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	bccRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(default=None,alias="bccRecipients",)
	body: Optional[ItemBody] = Field(default=None,alias="body",)
	bodyPreview: Optional[str] = Field(default=None,alias="bodyPreview",)
	ccRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(default=None,alias="ccRecipients",)
	conversationId: Optional[str] = Field(default=None,alias="conversationId",)
	conversationIndex: Optional[str] = Field(default=None,alias="conversationIndex",)
	flag: Optional[FollowupFlag] = Field(default=None,alias="flag",)
	from_: SerializeAsAny[Optional[Recipient]] = Field(default=None,alias="from",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	importance: Optional[Importance] = Field(default=None,alias="importance",)
	inferenceClassification: Optional[InferenceClassificationType] = Field(default=None,alias="inferenceClassification",)
	internetMessageHeaders: Optional[list[InternetMessageHeader]] = Field(default=None,alias="internetMessageHeaders",)
	internetMessageId: Optional[str] = Field(default=None,alias="internetMessageId",)
	isDeliveryReceiptRequested: Optional[bool] = Field(default=None,alias="isDeliveryReceiptRequested",)
	isDraft: Optional[bool] = Field(default=None,alias="isDraft",)
	isRead: Optional[bool] = Field(default=None,alias="isRead",)
	isReadReceiptRequested: Optional[bool] = Field(default=None,alias="isReadReceiptRequested",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	receivedDateTime: Optional[datetime] = Field(default=None,alias="receivedDateTime",)
	replyTo: SerializeAsAny[Optional[list[Recipient]]] = Field(default=None,alias="replyTo",)
	sender: SerializeAsAny[Optional[Recipient]] = Field(default=None,alias="sender",)
	sentDateTime: Optional[datetime] = Field(default=None,alias="sentDateTime",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	toRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(default=None,alias="toRecipients",)
	uniqueBody: Optional[ItemBody] = Field(default=None,alias="uniqueBody",)
	webLink: Optional[str] = Field(default=None,alias="webLink",)
	attachments: SerializeAsAny[Optional[list[Attachment]]] = Field(default=None,alias="attachments",)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(default=None,alias="extensions",)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(default=None,alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(default=None,alias="singleValueExtendedProperties",)
	canAccept: Optional[bool] = Field(default=None,alias="canAccept",)
	sharingMessageAction: Optional[CalendarSharingMessageAction] = Field(default=None,alias="sharingMessageAction",)
	sharingMessageActions: Optional[list[CalendarSharingMessageAction]] = Field(default=None,alias="sharingMessageActions",)
	suggestedCalendarName: Optional[str] = Field(default=None,alias="suggestedCalendarName",)

from .recipient import Recipient
from .item_body import ItemBody
from .recipient import Recipient
from .followup_flag import FollowupFlag
from .recipient import Recipient
from .importance import Importance
from .inference_classification_type import InferenceClassificationType
from .internet_message_header import InternetMessageHeader
from .recipient import Recipient
from .recipient import Recipient
from .recipient import Recipient
from .item_body import ItemBody
from .attachment import Attachment
from .extension import Extension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from .calendar_sharing_message_action import CalendarSharingMessageAction
from .calendar_sharing_message_action import CalendarSharingMessageAction

