from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EventMessage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	changeKey: Optional[str] = Field(alias="changeKey",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	bccRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="bccRecipients",default=None,)
	body: Optional[ItemBody] = Field(alias="body",default=None,)
	bodyPreview: Optional[str] = Field(alias="bodyPreview",default=None,)
	ccRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="ccRecipients",default=None,)
	conversationId: Optional[str] = Field(alias="conversationId",default=None,)
	conversationIndex: Optional[str] = Field(alias="conversationIndex",default=None,)
	flag: Optional[FollowupFlag] = Field(alias="flag",default=None,)
	from_: SerializeAsAny[Optional[Recipient]] = Field(alias="from",default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments",default=None,)
	importance: Optional[Importance | str] = Field(alias="importance",default=None,)
	inferenceClassification: Optional[InferenceClassificationType | str] = Field(alias="inferenceClassification",default=None,)
	internetMessageHeaders: Optional[list[InternetMessageHeader]] = Field(alias="internetMessageHeaders",default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId",default=None,)
	isDeliveryReceiptRequested: Optional[bool] = Field(alias="isDeliveryReceiptRequested",default=None,)
	isDraft: Optional[bool] = Field(alias="isDraft",default=None,)
	isRead: Optional[bool] = Field(alias="isRead",default=None,)
	isReadReceiptRequested: Optional[bool] = Field(alias="isReadReceiptRequested",default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId",default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime",default=None,)
	replyTo: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="replyTo",default=None,)
	sender: SerializeAsAny[Optional[Recipient]] = Field(alias="sender",default=None,)
	sentDateTime: Optional[datetime] = Field(alias="sentDateTime",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	toRecipients: SerializeAsAny[Optional[list[Recipient]]] = Field(alias="toRecipients",default=None,)
	uniqueBody: Optional[ItemBody] = Field(alias="uniqueBody",default=None,)
	webLink: Optional[str] = Field(alias="webLink",default=None,)
	attachments: SerializeAsAny[Optional[list[Attachment]]] = Field(alias="attachments",default=None,)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(alias="extensions",default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties",default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties",default=None,)
	endDateTime: Optional[DateTimeTimeZone] = Field(alias="endDateTime",default=None,)
	isAllDay: Optional[bool] = Field(alias="isAllDay",default=None,)
	isDelegated: Optional[bool] = Field(alias="isDelegated",default=None,)
	isOutOfDate: Optional[bool] = Field(alias="isOutOfDate",default=None,)
	location: SerializeAsAny[Optional[Location]] = Field(alias="location",default=None,)
	meetingMessageType: Optional[MeetingMessageType | str] = Field(alias="meetingMessageType",default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence",default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime",default=None,)
	type: Optional[EventType | str] = Field(alias="type",default=None,)
	event: Optional[Event] = Field(alias="event",default=None,)

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

