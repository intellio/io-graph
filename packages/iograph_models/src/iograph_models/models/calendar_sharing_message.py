from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CalendarSharingMessage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	categories: list[Optional[str]] = Field(alias="categories",)
	changeKey: Optional[str] = Field(default=None,alias="changeKey",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	bccRecipients: list[Recipient] = Field(alias="bccRecipients",)
	body: Optional[ItemBody] = Field(default=None,alias="body",)
	bodyPreview: Optional[str] = Field(default=None,alias="bodyPreview",)
	ccRecipients: list[Recipient] = Field(alias="ccRecipients",)
	conversationId: Optional[str] = Field(default=None,alias="conversationId",)
	conversationIndex: Optional[str] = Field(default=None,alias="conversationIndex",)
	flag: Optional[FollowupFlag] = Field(default=None,alias="flag",)
	from_: Optional[Recipient] = Field(default=None,alias="from",)
	hasAttachments: Optional[bool] = Field(default=None,alias="hasAttachments",)
	importance: Optional[Importance] = Field(default=None,alias="importance",)
	inferenceClassification: Optional[InferenceClassificationType] = Field(default=None,alias="inferenceClassification",)
	internetMessageHeaders: list[InternetMessageHeader] = Field(alias="internetMessageHeaders",)
	internetMessageId: Optional[str] = Field(default=None,alias="internetMessageId",)
	isDeliveryReceiptRequested: Optional[bool] = Field(default=None,alias="isDeliveryReceiptRequested",)
	isDraft: Optional[bool] = Field(default=None,alias="isDraft",)
	isRead: Optional[bool] = Field(default=None,alias="isRead",)
	isReadReceiptRequested: Optional[bool] = Field(default=None,alias="isReadReceiptRequested",)
	parentFolderId: Optional[str] = Field(default=None,alias="parentFolderId",)
	receivedDateTime: Optional[datetime] = Field(default=None,alias="receivedDateTime",)
	replyTo: list[Recipient] = Field(alias="replyTo",)
	sender: Optional[Recipient] = Field(default=None,alias="sender",)
	sentDateTime: Optional[datetime] = Field(default=None,alias="sentDateTime",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	toRecipients: list[Recipient] = Field(alias="toRecipients",)
	uniqueBody: Optional[ItemBody] = Field(default=None,alias="uniqueBody",)
	webLink: Optional[str] = Field(default=None,alias="webLink",)
	attachments: list[Attachment] = Field(alias="attachments",)
	extensions: list[Extension] = Field(alias="extensions",)
	multiValueExtendedProperties: list[MultiValueLegacyExtendedProperty] = Field(alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: list[SingleValueLegacyExtendedProperty] = Field(alias="singleValueExtendedProperties",)
	canAccept: Optional[bool] = Field(default=None,alias="canAccept",)
	sharingMessageAction: Optional[CalendarSharingMessageAction] = Field(default=None,alias="sharingMessageAction",)
	sharingMessageActions: list[CalendarSharingMessageAction] = Field(alias="sharingMessageActions",)
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

