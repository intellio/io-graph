from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Message(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.message"] = Field(alias="@odata.type", default="#microsoft.graph.message")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	bccRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee],Field(discriminator="odata_type")]]] = Field(alias="bccRecipients", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	bodyPreview: Optional[str] = Field(alias="bodyPreview", default=None,)
	ccRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee],Field(discriminator="odata_type")]]] = Field(alias="ccRecipients", default=None,)
	conversationId: Optional[str] = Field(alias="conversationId", default=None,)
	conversationIndex: Optional[str] = Field(alias="conversationIndex", default=None,)
	flag: Optional[FollowupFlag] = Field(alias="flag", default=None,)
	from_: Optional[Union[AttendeeBase, Attendee]] = Field(alias="from", default=None,discriminator="odata_type", )
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	importance: Optional[Importance | str] = Field(alias="importance", default=None,)
	inferenceClassification: Optional[InferenceClassificationType | str] = Field(alias="inferenceClassification", default=None,)
	internetMessageHeaders: Optional[list[InternetMessageHeader]] = Field(alias="internetMessageHeaders", default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId", default=None,)
	isDeliveryReceiptRequested: Optional[bool] = Field(alias="isDeliveryReceiptRequested", default=None,)
	isDraft: Optional[bool] = Field(alias="isDraft", default=None,)
	isRead: Optional[bool] = Field(alias="isRead", default=None,)
	isReadReceiptRequested: Optional[bool] = Field(alias="isReadReceiptRequested", default=None,)
	mentionsPreview: Optional[MentionsPreview] = Field(alias="mentionsPreview", default=None,)
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	replyTo: Optional[list[Annotated[Union[AttendeeBase, Attendee],Field(discriminator="odata_type")]]] = Field(alias="replyTo", default=None,)
	sender: Optional[Union[AttendeeBase, Attendee]] = Field(alias="sender", default=None,discriminator="odata_type", )
	sentDateTime: Optional[datetime] = Field(alias="sentDateTime", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	toRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee],Field(discriminator="odata_type")]]] = Field(alias="toRecipients", default=None,)
	uniqueBody: Optional[ItemBody] = Field(alias="uniqueBody", default=None,)
	unsubscribeData: Optional[list[str]] = Field(alias="unsubscribeData", default=None,)
	unsubscribeEnabled: Optional[bool] = Field(alias="unsubscribeEnabled", default=None,)
	webLink: Optional[str] = Field(alias="webLink", default=None,)
	attachments: Optional[list[Annotated[Union[FileAttachment, ItemAttachment, ReferenceAttachment],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension, PersonExtension],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	mentions: Optional[list[Mention]] = Field(alias="mentions", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

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
			if mapping_key == "#microsoft.graph.calendarSharingMessage":
				from .calendar_sharing_message import CalendarSharingMessage
				return CalendarSharingMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessage":
				from .event_message import EventMessage
				return EventMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessageRequest":
				from .event_message_request import EventMessageRequest
				return EventMessageRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessageResponse":
				from .event_message_response import EventMessageResponse
				return EventMessageResponse.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .attendee_base import AttendeeBase
from .attendee import Attendee
from .item_body import ItemBody
from .attendee_base import AttendeeBase
from .attendee import Attendee
from .followup_flag import FollowupFlag
from .attendee_base import AttendeeBase
from .attendee import Attendee
from .importance import Importance
from .inference_classification_type import InferenceClassificationType
from .internet_message_header import InternetMessageHeader
from .mentions_preview import MentionsPreview
from .attendee_base import AttendeeBase
from .attendee import Attendee
from .attendee_base import AttendeeBase
from .attendee import Attendee
from .attendee_base import AttendeeBase
from .attendee import Attendee
from .item_body import ItemBody
from .file_attachment import FileAttachment
from .item_attachment import ItemAttachment
from .reference_attachment import ReferenceAttachment
from .open_type_extension import OpenTypeExtension
from .person_extension import PersonExtension
from .mention import Mention
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

