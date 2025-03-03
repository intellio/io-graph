from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class BookingBusiness(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	address: Optional[PhysicalAddress] = Field(default=None,alias="address",)
	bookingPageSettings: Optional[BookingPageSettings] = Field(default=None,alias="bookingPageSettings",)
	businessHours: Optional[list[BookingWorkHours]] = Field(default=None,alias="businessHours",)
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
	appointments: Optional[list[BookingAppointment]] = Field(default=None,alias="appointments",)
	calendarView: Optional[list[BookingAppointment]] = Field(default=None,alias="calendarView",)
	customers: Optional[list[BookingCustomerBase]] = Field(default=None,alias="customers",)
	customQuestions: Optional[list[BookingCustomQuestion]] = Field(default=None,alias="customQuestions",)
	services: Optional[list[BookingService]] = Field(default=None,alias="services",)
	staffMembers: Optional[list[BookingStaffMemberBase]] = Field(default=None,alias="staffMembers",)

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

