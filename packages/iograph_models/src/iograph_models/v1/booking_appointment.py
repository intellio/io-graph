from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class BookingAppointment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.bookingAppointment"] = Field(alias="@odata.type", default="#microsoft.graph.bookingAppointment")
	additionalInformation: Optional[str] = Field(alias="additionalInformation", default=None,)
	anonymousJoinWebUrl: Optional[str] = Field(alias="anonymousJoinWebUrl", default=None,)
	appointmentLabel: Optional[str] = Field(alias="appointmentLabel", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customerEmailAddress: Optional[str] = Field(alias="customerEmailAddress", default=None,)
	customerName: Optional[str] = Field(alias="customerName", default=None,)
	customerNotes: Optional[str] = Field(alias="customerNotes", default=None,)
	customerPhone: Optional[str] = Field(alias="customerPhone", default=None,)
	customers: Optional[list[Annotated[Union[BookingCustomerInformation],Field(discriminator="odata_type")]]] = Field(alias="customers", default=None,)
	customerTimeZone: Optional[str] = Field(alias="customerTimeZone", default=None,)
	duration: Optional[str] = Field(alias="duration", default=None,)
	endDateTime: Optional[DateTimeTimeZone] = Field(alias="endDateTime", default=None,)
	filledAttendeesCount: Optional[int] = Field(alias="filledAttendeesCount", default=None,)
	isCustomerAllowedToManageBooking: Optional[bool] = Field(alias="isCustomerAllowedToManageBooking", default=None,)
	isLocationOnline: Optional[bool] = Field(alias="isLocationOnline", default=None,)
	joinWebUrl: Optional[str] = Field(alias="joinWebUrl", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	maximumAttendeesCount: Optional[int] = Field(alias="maximumAttendeesCount", default=None,)
	optOutOfCustomerEmail: Optional[bool] = Field(alias="optOutOfCustomerEmail", default=None,)
	postBuffer: Optional[str] = Field(alias="postBuffer", default=None,)
	preBuffer: Optional[str] = Field(alias="preBuffer", default=None,)
	price: float | str | ReferenceNumeric
	priceType: Optional[BookingPriceType | str] = Field(alias="priceType", default=None,)
	reminders: Optional[list[BookingReminder]] = Field(alias="reminders", default=None,)
	selfServiceAppointmentId: Optional[str] = Field(alias="selfServiceAppointmentId", default=None,)
	serviceId: Optional[str] = Field(alias="serviceId", default=None,)
	serviceLocation: Optional[Union[LocationConstraintItem]] = Field(alias="serviceLocation", default=None,discriminator="odata_type", )
	serviceName: Optional[str] = Field(alias="serviceName", default=None,)
	serviceNotes: Optional[str] = Field(alias="serviceNotes", default=None,)
	smsNotificationsEnabled: Optional[bool] = Field(alias="smsNotificationsEnabled", default=None,)
	staffMemberIds: Optional[list[str]] = Field(alias="staffMemberIds", default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime", default=None,)

from .booking_customer_information import BookingCustomerInformation
from .date_time_time_zone import DateTimeTimeZone
from .reference_numeric import ReferenceNumeric
from .booking_price_type import BookingPriceType
from .booking_reminder import BookingReminder
from .location_constraint_item import LocationConstraintItem
