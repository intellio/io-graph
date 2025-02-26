from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BookingBusiness(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	bookingPageSettings: Optional[BookingPageSettings] = Field(default=None,alias="bookingPageSettings",)
	businessHours: list[BookingWorkHours] = Field(alias="businessHours",)
	businessType: Optional[str] = Field(default=None,alias="businessType",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	defaultCurrencyIso: Optional[str] = Field(default=None,alias="defaultCurrencyIso",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	email: Optional[str] = Field(default=None,alias="email",)
	isPublished: Optional[bool] = Field(default=None,alias="isPublished",)
	languageTag: Optional[str] = Field(default=None,alias="languageTag",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	phone: Optional[str] = Field(default=None,alias="phone",)
	publicUrl: Optional[str] = Field(default=None,alias="publicUrl",)
	schedulingPolicy: Optional[BookingSchedulingPolicy] = Field(default=None,alias="schedulingPolicy",)
	webSiteUrl: Optional[str] = Field(default=None,alias="webSiteUrl",)
	appointments: list[BookingAppointment] = Field(alias="appointments",)
	calendarView: list[BookingAppointment] = Field(alias="calendarView",)
	customers: list[BookingCustomerBase] = Field(alias="customers",)
	customQuestions: list[BookingCustomQuestion] = Field(alias="customQuestions",)
	services: list[BookingService] = Field(alias="services",)
	staffMembers: list[BookingStaffMemberBase] = Field(alias="staffMembers",)

from .physical_address import PhysicalAddress
from .booking_page_settings import BookingPageSettings
from .booking_work_hours import BookingWorkHours
from .booking_scheduling_policy import BookingSchedulingPolicy
from .booking_appointment import BookingAppointment
from .booking_appointment import BookingAppointment
from .booking_customer_base import BookingCustomerBase
from .booking_custom_question import BookingCustomQuestion
from .booking_service import BookingService
from .booking_staff_member_base import BookingStaffMemberBase

