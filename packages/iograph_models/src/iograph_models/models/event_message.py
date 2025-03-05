from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EventMessage(BaseModel):
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
	attachments: Optional[list[Attachment]] = Field(default=None,alias="attachments",)
	extensions: Optional[list[Extension]] = Field(default=None,alias="extensions",)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(default=None,alias="multiValueExtendedProperties",)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(default=None,alias="singleValueExtendedProperties",)
	endDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="endDateTime",)
	isAllDay: Optional[bool] = Field(default=None,alias="isAllDay",)
	isDelegated: Optional[bool] = Field(default=None,alias="isDelegated",)
	isOutOfDate: Optional[bool] = Field(default=None,alias="isOutOfDate",)
	location: SerializeAsAny[Optional[Location]] = Field(default=None,alias="location",)
	meetingMessageType: Optional[MeetingMessageType] = Field(default=None,alias="meetingMessageType",)
	recurrence: Optional[PatternedRecurrence] = Field(default=None,alias="recurrence",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)
	type: Optional[EventType] = Field(default=None,alias="type",)
	event: Optional[Event] = Field(default=None,alias="event",)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.eventMessageRequest":
				from .event_message_request import EventMessageRequest
				return EventMessageRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessageResponse":
				from .event_message_response import EventMessageResponse
				return EventMessageResponse.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

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
from .date_time_time_zone import DateTimeTimeZone
from .location import Location
from .meeting_message_type import MeetingMessageType
from .patterned_recurrence import PatternedRecurrence
from .date_time_time_zone import DateTimeTimeZone
from .event_type import EventType
from .event import Event

