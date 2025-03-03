from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BookingAppointment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	additionalInformation: Optional[str] = Field(default=None,alias="additionalInformation",)
	anonymousJoinWebUrl: Optional[str] = Field(default=None,alias="anonymousJoinWebUrl",)
	appointmentLabel: Optional[str] = Field(default=None,alias="appointmentLabel",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	customerEmailAddress: Optional[str] = Field(default=None,alias="customerEmailAddress",)
	customerName: Optional[str] = Field(default=None,alias="customerName",)
	customerNotes: Optional[str] = Field(default=None,alias="customerNotes",)
	customerPhone: Optional[str] = Field(default=None,alias="customerPhone",)
	customers: Optional[list[BookingCustomerInformationBase]] = Field(default=None,alias="customers",)
	customerTimeZone: Optional[str] = Field(default=None,alias="customerTimeZone",)
	duration: Optional[str] = Field(default=None,alias="duration",)
	endDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="endDateTime",)
	filledAttendeesCount: Optional[int] = Field(default=None,alias="filledAttendeesCount",)
	isCustomerAllowedToManageBooking: Optional[bool] = Field(default=None,alias="isCustomerAllowedToManageBooking",)
	isLocationOnline: Optional[bool] = Field(default=None,alias="isLocationOnline",)
	joinWebUrl: Optional[str] = Field(default=None,alias="joinWebUrl",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	maximumAttendeesCount: Optional[int] = Field(default=None,alias="maximumAttendeesCount",)
	optOutOfCustomerEmail: Optional[bool] = Field(default=None,alias="optOutOfCustomerEmail",)
	postBuffer: Optional[str] = Field(default=None,alias="postBuffer",)
	preBuffer: Optional[str] = Field(default=None,alias="preBuffer",)
	price: float | str | ReferenceNumeric
	priceType: Optional[BookingPriceType] = Field(default=None,alias="priceType",)
	reminders: Optional[list[BookingReminder]] = Field(default=None,alias="reminders",)
	selfServiceAppointmentId: Optional[str] = Field(default=None,alias="selfServiceAppointmentId",)
	serviceId: Optional[str] = Field(default=None,alias="serviceId",)
	serviceLocation: Optional[Location] = Field(default=None,alias="serviceLocation",)
	serviceName: Optional[str] = Field(default=None,alias="serviceName",)
	serviceNotes: Optional[str] = Field(default=None,alias="serviceNotes",)
	smsNotificationsEnabled: Optional[bool] = Field(default=None,alias="smsNotificationsEnabled",)
	staffMemberIds: Optional[list[str]] = Field(default=None,alias="staffMemberIds",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)

from .booking_customer_information_base import BookingCustomerInformationBase
from .date_time_time_zone import DateTimeTimeZone
from .reference_numeric import ReferenceNumeric
from .booking_price_type import BookingPriceType
from .booking_reminder import BookingReminder
from .location import Location
from .date_time_time_zone import DateTimeTimeZone

