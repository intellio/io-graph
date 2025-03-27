from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class BookingBusiness(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	address: Optional[PhysicalAddress] = Field(alias="address", default=None,)
	bookingPageSettings: Optional[BookingPageSettings] = Field(alias="bookingPageSettings", default=None,)
	businessHours: Optional[list[BookingWorkHours]] = Field(alias="businessHours", default=None,)
	businessType: Optional[str] = Field(alias="businessType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	defaultCurrencyIso: Optional[str] = Field(alias="defaultCurrencyIso", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	isPublished: Optional[bool] = Field(alias="isPublished", default=None,)
	languageTag: Optional[str] = Field(alias="languageTag", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	phone: Optional[str] = Field(alias="phone", default=None,)
	publicUrl: Optional[str] = Field(alias="publicUrl", default=None,)
	schedulingPolicy: Optional[BookingSchedulingPolicy] = Field(alias="schedulingPolicy", default=None,)
	webSiteUrl: Optional[str] = Field(alias="webSiteUrl", default=None,)
	appointments: Optional[list[BookingAppointment]] = Field(alias="appointments", default=None,)
	calendarView: Optional[list[BookingAppointment]] = Field(alias="calendarView", default=None,)
	customers: Optional[list[Annotated[Union[BookingCustomer]],Field(discriminator="odata_type")]]] = Field(alias="customers", default=None,)
	customQuestions: Optional[list[BookingCustomQuestion]] = Field(alias="customQuestions", default=None,)
	services: Optional[list[BookingService]] = Field(alias="services", default=None,)
	staffMembers: Optional[list[Annotated[Union[BookingStaffMember]],Field(discriminator="odata_type")]]] = Field(alias="staffMembers", default=None,)

from .physical_address import PhysicalAddress
from .booking_page_settings import BookingPageSettings
from .booking_work_hours import BookingWorkHours
from .booking_scheduling_policy import BookingSchedulingPolicy
from .booking_appointment import BookingAppointment
from .booking_appointment import BookingAppointment
from .booking_customer import BookingCustomer
from .booking_custom_question import BookingCustomQuestion
from .booking_service import BookingService
from .booking_staff_member import BookingStaffMember

