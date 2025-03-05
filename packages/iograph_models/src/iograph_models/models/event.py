from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Event(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	categories: Optional[list[str]] = Field(alias="categories",default=None,)
	changeKey: Optional[str] = Field(alias="changeKey",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	allowNewTimeProposals: Optional[bool] = Field(alias="allowNewTimeProposals",default=None,)
	attendees: Optional[list[Attendee]] = Field(alias="attendees",default=None,)
	body: Optional[ItemBody] = Field(alias="body",default=None,)
	bodyPreview: Optional[str] = Field(alias="bodyPreview",default=None,)
	end: Optional[DateTimeTimeZone] = Field(alias="end",default=None,)
	hasAttachments: Optional[bool] = Field(alias="hasAttachments",default=None,)
	hideAttendees: Optional[bool] = Field(alias="hideAttendees",default=None,)
	iCalUId: Optional[str] = Field(alias="iCalUId",default=None,)
	importance: Optional[Importance | str] = Field(alias="importance",default=None,)
	isAllDay: Optional[bool] = Field(alias="isAllDay",default=None,)
	isCancelled: Optional[bool] = Field(alias="isCancelled",default=None,)
	isDraft: Optional[bool] = Field(alias="isDraft",default=None,)
	isOnlineMeeting: Optional[bool] = Field(alias="isOnlineMeeting",default=None,)
	isOrganizer: Optional[bool] = Field(alias="isOrganizer",default=None,)
	isReminderOn: Optional[bool] = Field(alias="isReminderOn",default=None,)
	location: SerializeAsAny[Optional[Location]] = Field(alias="location",default=None,)
	locations: SerializeAsAny[Optional[list[Location]]] = Field(alias="locations",default=None,)
	onlineMeeting: Optional[OnlineMeetingInfo] = Field(alias="onlineMeeting",default=None,)
	onlineMeetingProvider: Optional[OnlineMeetingProviderType | str] = Field(alias="onlineMeetingProvider",default=None,)
	onlineMeetingUrl: Optional[str] = Field(alias="onlineMeetingUrl",default=None,)
	organizer: SerializeAsAny[Optional[Recipient]] = Field(alias="organizer",default=None,)
	originalEndTimeZone: Optional[str] = Field(alias="originalEndTimeZone",default=None,)
	originalStart: Optional[datetime] = Field(alias="originalStart",default=None,)
	originalStartTimeZone: Optional[str] = Field(alias="originalStartTimeZone",default=None,)
	recurrence: Optional[PatternedRecurrence] = Field(alias="recurrence",default=None,)
	reminderMinutesBeforeStart: Optional[int] = Field(alias="reminderMinutesBeforeStart",default=None,)
	responseRequested: Optional[bool] = Field(alias="responseRequested",default=None,)
	responseStatus: Optional[ResponseStatus] = Field(alias="responseStatus",default=None,)
	sensitivity: Optional[Sensitivity | str] = Field(alias="sensitivity",default=None,)
	seriesMasterId: Optional[str] = Field(alias="seriesMasterId",default=None,)
	showAs: Optional[FreeBusyStatus | str] = Field(alias="showAs",default=None,)
	start: Optional[DateTimeTimeZone] = Field(alias="start",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	transactionId: Optional[str] = Field(alias="transactionId",default=None,)
	type: Optional[EventType | str] = Field(alias="type",default=None,)
	webLink: Optional[str] = Field(alias="webLink",default=None,)
	attachments: SerializeAsAny[Optional[list[Attachment]]] = Field(alias="attachments",default=None,)
	calendar: Optional[Calendar] = Field(alias="calendar",default=None,)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(alias="extensions",default=None,)
	instances: Optional[list[Event]] = Field(alias="instances",default=None,)
	multiValueExtendedProperties: Optional[list[MultiValueLegacyExtendedProperty]] = Field(alias="multiValueExtendedProperties",default=None,)
	singleValueExtendedProperties: Optional[list[SingleValueLegacyExtendedProperty]] = Field(alias="singleValueExtendedProperties",default=None,)

from .attendee import Attendee
from .item_body import ItemBody
from .date_time_time_zone import DateTimeTimeZone
from .importance import Importance
from .location import Location
from .location import Location
from .online_meeting_info import OnlineMeetingInfo
from .online_meeting_provider_type import OnlineMeetingProviderType
from .recipient import Recipient
from .patterned_recurrence import PatternedRecurrence
from .response_status import ResponseStatus
from .sensitivity import Sensitivity
from .free_busy_status import FreeBusyStatus
from .date_time_time_zone import DateTimeTimeZone
from .event_type import EventType
from .attachment import Attachment
from .calendar import Calendar
from .extension import Extension
from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

