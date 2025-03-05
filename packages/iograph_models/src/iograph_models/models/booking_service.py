from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BookingService(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	additionalInformation: Optional[str] = Field(default=None,alias="additionalInformation",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customQuestions: Optional[list[BookingQuestionAssignment]] = Field(default=None,alias="customQuestions",)
	defaultDuration: Optional[str] = Field(default=None,alias="defaultDuration",)
	defaultLocation: SerializeAsAny[Optional[Location]] = Field(default=None,alias="defaultLocation",)
	defaultPrice: float | str | ReferenceNumeric
	defaultPriceType: Optional[BookingPriceType] = Field(default=None,alias="defaultPriceType",)
	defaultReminders: Optional[list[BookingReminder]] = Field(default=None,alias="defaultReminders",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isAnonymousJoinEnabled: Optional[bool] = Field(default=None,alias="isAnonymousJoinEnabled",)
	isCustomerAllowedToManageBooking: Optional[bool] = Field(default=None,alias="isCustomerAllowedToManageBooking",)
	isHiddenFromCustomers: Optional[bool] = Field(default=None,alias="isHiddenFromCustomers",)
	isLocationOnline: Optional[bool] = Field(default=None,alias="isLocationOnline",)
	languageTag: Optional[str] = Field(default=None,alias="languageTag",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	maximumAttendeesCount: Optional[int] = Field(default=None,alias="maximumAttendeesCount",)
	notes: Optional[str] = Field(default=None,alias="notes",)
	postBuffer: Optional[str] = Field(default=None,alias="postBuffer",)
	preBuffer: Optional[str] = Field(default=None,alias="preBuffer",)
	schedulingPolicy: Optional[BookingSchedulingPolicy] = Field(default=None,alias="schedulingPolicy",)
	smsNotificationsEnabled: Optional[bool] = Field(default=None,alias="smsNotificationsEnabled",)
	staffMemberIds: Optional[list[str]] = Field(default=None,alias="staffMemberIds",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)

from .booking_question_assignment import BookingQuestionAssignment
from .location import Location
from .reference_numeric import ReferenceNumeric
from .booking_price_type import BookingPriceType
from .booking_reminder import BookingReminder
from .booking_scheduling_policy import BookingSchedulingPolicy

