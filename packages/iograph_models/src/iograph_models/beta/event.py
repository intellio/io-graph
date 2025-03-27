from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Event(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.event"] = Field(alias="@odata.type", default="#microsoft.graph.event")
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	allowNewTimeProposals: Optional[bool] = Field(alias="allowNewTimeProposals", default=None,)
	attendees: Optional[list[Attendee]] = Field(alias="attendees", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	bodyPreview: Optional[str] = Field(alias="bodyPreview", default=None,)
	cancelledOccurrences: Optional[list[str]] = Field(alias="cancelledOccurrences", default=None,)
	end: Optional[DateTimeTimeZone] = Field(alias="end", default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments", default=None,)
	hideAttendees: Optional[bool] = Field(alias="hideAttendees", default=None,)
	iCalUId: Optional[str] = Field(alias="iCalUId", default=None,)
	importance: Optional[Importance | str] = Field(alias="importance", default=None,)
	isAllDay: Optional[bool] = Field(alias="isAllDay", default=None,)
	isCancelled: Optional[bool] = Field(alias="isCancelled", default=None,)
	isDraft: Optional[bool] = Field(alias="isDraft", default=None,)
	isOnlineMeeting: Optional[bool] = Field(alias="isOnlineMeeting", default=None,)
	isOrganizer: Optional[bool] = Field(alias="isOrganizer", default=None,)
	isReminderOn: Optional[bool] = Field(alias="isReminderOn", default=None,)
	location: Optional[Union[LocationConstraintItem]] = Field(alias="location", default=None,discriminator="odata_type", )
	locations: Optional[list[Annotated[Union[LocationConstraintItem]],Field(discriminator="odata_type")]]] = Field(alias="locations", default=None,)
	occurrenceId: Optional[str] = Field(alias="occurrenceId", default=None,)
	onlineMeeting: Optional[OnlineMeetingInfo] = Field(alias="onlineMeeting", default=None,)
	onlineMeetingProvider: Optional[OnlineMeetingProviderType | str] = Field(alias="onlineMeetingProvider", default=None,)
	onlineMeetingUrl: Optional[str] = Field(alias="onlineMeetingUrl", default=None,)
	organizer: Optional[Union[AttendeeBase, Attendee]] = Field(alias="organizer", default=None,discriminator="odata_type", )
	originalEndTimeZone: Optional[str] = Field(alias="originalEndTimeZone", default=None,)
	originalStart: Optional[datetime] = Field(alias="originalStart", default=None,)
	originalStartTimeZone: Optional[str] = Field(alias="originalStartTimeZone", default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence", default=None,)
	reminderMinutesBeforeStart: Optional[int] = Field(alias="reminderMinutesBeforeStart", default=None,)
	responseRequested: Optional[bool] = Field(alias="responseRequested", default=None,)
	responseStatus: Optional[ResponseStatus] = Field(alias="responseStatus", default=None,)
	sensitivity: Optional[Sensitivity | str] = Field(alias="sensitivity", default=None,)
	seriesMasterId: Optional[str] = Field(alias="seriesMasterId", default=None,)
	showAs: Optional[FreeBusyStatus | str] = Field(alias="showAs", default=None,)
	start: Optional[DateTimeTimeZone] = Field(alias="start", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	transactionId: Optional[str] = Field(alias="transactionId", default=None,)
	type: Optional[EventType | str] = Field(alias="type", default=None,)
	uid: Optional[str] = Field(alias="uid", default=None,)
	webLink: Optional[str] = Field(alias="webLink", default=None,)
	attachments: Optional[list[Annotated[Union[FileAttachment, ItemAttachment, ReferenceAttachment]],Field(discriminator="odata_type")]]] = Field(alias="attachments", default=None,)
	calendar: Optional[Calendar] = Field(alias="calendar", default=None,)
	exceptionOccurrences: Optional[list[Event]] = Field(alias="exceptionOccurrences", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension, PersonExtension]],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)
	instances: Optional[list[Event]] = Field(alias="instances", default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties", default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties", default=None,)

from .attendee import Attendee
from .item_body import ItemBody
from .date_time_time_zone import DateTimeTimeZone
from .importance import Importance
from .location_constraint_item import LocationConstraintItem
from .location_constraint_item import LocationConstraintItem
from .online_meeting_info import OnlineMeetingInfo
from .online_meeting_provider_type import OnlineMeetingProviderType
from .attendee_base import AttendeeBase
from .attendee import Attendee
from .patterned_recurrence import PatternedRecurrence
from .response_status import ResponseStatus
from .sensitivity import Sensitivity
from .free_busy_status import FreeBusyStatus
from .date_time_time_zone import DateTimeTimeZone
from .event_type import EventType
from .file_attachment import FileAttachment
from .item_attachment import ItemAttachment
from .reference_attachment import ReferenceAttachment
from .calendar import Calendar
from .open_type_extension import OpenTypeExtension
from .person_extension import PersonExtension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

