from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EventMessageRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.eventMessageRequest"] = Field(alias="@odata.type", default="#microsoft.graph.eventMessageRequest")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	bccRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee]],Field(discriminator="odata_type")]]] = Field(alias="bccRecipients", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	bodyPreview: Optional[str] = Field(alias="bodyPreview", default=None,)
	ccRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee]],Field(discriminator="odata_type")]]] = Field(alias="ccRecipients", default=None,)
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
	parentFolderId: Optional[str] = Field(alias="parentFolderId", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	replyTo: Optional[list[Annotated[Union[AttendeeBase, Attendee]],Field(discriminator="odata_type")]]] = Field(alias="replyTo", default=None,)
	sender: Optional[Union[AttendeeBase, Attendee]] = Field(alias="sender", default=None,discriminator="odata_type", )
	sentDateTime: Optional[datetime] = Field(alias="sentDateTime", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	toRecipients: Optional[list[Annotated[Union[AttendeeBase, Attendee]],Field(discriminator="odata_type")]]] = Field(alias="toRecipients", default=None,)
	uniqueBody: Optional[ItemBody] = Field(alias="uniqueBody", default=None,)
	webLink: Optional[str] = Field(alias="webLink", default=None,)
	attachments: Optional[list[Annotated[Union[FileAttachment, ItemAttachment, ReferenceAttachment]],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension]],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)
	endDateTime: Optional[DateTimeTimeZone] = Field(alias="endDateTime", default=None,)
	isAllDay: Optional[bool] = Field(alias="isAllDay", default=None,)
	isDelegated: Optional[bool] = Field(alias="isDelegated", default=None,)
	isOutOfDate: Optional[bool] = Field(alias="isOutOfDate", default=None,)
	location: Optional[Union[LocationConstraintItem]] = Field(alias="location", default=None,discriminator="odata_type", )
	meetingMessageType: Optional[MeetingMessageType | str] = Field(alias="meetingMessageType", default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence", default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime", default=None,)
	type: Optional[EventType | str] = Field(alias="type", default=None,)
	event: Optional[Event] = Field(alias="event", default=None,)
	allowNewTimeProposals: Optional[bool] = Field(alias="allowNewTimeProposals", default=None,)
	meetingRequestType: Optional[MeetingRequestType | str] = Field(alias="meetingRequestType", default=None,)
	previousEndDateTime: Optional[DateTimeTimeZone] = Field(alias="previousEndDateTime", default=None,)
	previousLocation: Optional[Union[LocationConstraintItem]] = Field(alias="previousLocation", default=None,discriminator="odata_type", )
	previousStartDateTime: Optional[DateTimeTimeZone] = Field(alias="previousStartDateTime", default=None,)
	responseRequested: Optional[bool] = Field(alias="responseRequested", default=None,)

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
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from .date_time_time_zone import DateTimeTimeZone
from .location_constraint_item import LocationConstraintItem
from .meeting_message_type import MeetingMessageType
from .patterned_recurrence import PatternedRecurrence
from .date_time_time_zone import DateTimeTimeZone
from .event_type import EventType
from .event import Event
from .meeting_request_type import MeetingRequestType
from .date_time_time_zone import DateTimeTimeZone
from .location_constraint_item import LocationConstraintItem
from .date_time_time_zone import DateTimeTimeZone

