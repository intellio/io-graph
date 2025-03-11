from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BookingService(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	additionalInformation: Optional[str] = Field(alias="additionalInformation",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	customQuestions: Optional[list[BookingQuestionAssignment]] = Field(alias="customQuestions",default=None,)
	defaultDuration: Optional[str] = Field(alias="defaultDuration",default=None,)
	defaultLocation: SerializeAsAny[Optional[Location]] = Field(alias="defaultLocation",default=None,)
	defaultPrice: float | str | ReferenceNumeric
	defaultPriceType: Optional[BookingPriceType | str] = Field(alias="defaultPriceType",default=None,)
	defaultReminders: Optional[list[BookingReminder]] = Field(alias="defaultReminders",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isAnonymousJoinEnabled: Optional[bool] = Field(alias="isAnonymousJoinEnabled",default=None,)
	isCustomerAllowedToManageBooking: Optional[bool] = Field(alias="isCustomerAllowedToManageBooking",default=None,)
	isHiddenFromCustomers: Optional[bool] = Field(alias="isHiddenFromCustomers",default=None,)
	isLocationOnline: Optional[bool] = Field(alias="isLocationOnline",default=None,)
	languageTag: Optional[str] = Field(alias="languageTag",default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime",default=None,)
	maximumAttendeesCount: Optional[int] = Field(alias="maximumAttendeesCount",default=None,)
	notes: Optional[str] = Field(alias="notes",default=None,)
	postBuffer: Optional[str] = Field(alias="postBuffer",default=None,)
	preBuffer: Optional[str] = Field(alias="preBuffer",default=None,)
	schedulingPolicy: Optional[BookingSchedulingPolicy] = Field(alias="schedulingPolicy",default=None,)
	smsNotificationsEnabled: Optional[bool] = Field(alias="smsNotificationsEnabled",default=None,)
	staffMemberIds: Optional[list[str]] = Field(alias="staffMemberIds",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)

from .booking_question_assignment import BookingQuestionAssignment
from .location import Location
from .reference_numeric import ReferenceNumeric
from .booking_price_type import BookingPriceType
from .booking_reminder import BookingReminder
from .booking_scheduling_policy import BookingSchedulingPolicy

