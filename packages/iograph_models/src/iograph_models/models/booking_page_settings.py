from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingPageSettings(BaseModel):
	accessControl: Optional[BookingPageAccessControl] = Field(default=None,alias="accessControl",)
	bookingPageColorCode: Optional[str] = Field(default=None,alias="bookingPageColorCode",)
	businessTimeZone: Optional[str] = Field(default=None,alias="businessTimeZone",)
	customerConsentMessage: Optional[str] = Field(default=None,alias="customerConsentMessage",)
	enforceOneTimePassword: Optional[bool] = Field(default=None,alias="enforceOneTimePassword",)
	isBusinessLogoDisplayEnabled: Optional[bool] = Field(default=None,alias="isBusinessLogoDisplayEnabled",)
	isCustomerConsentEnabled: Optional[bool] = Field(default=None,alias="isCustomerConsentEnabled",)
	isSearchEngineIndexabilityDisabled: Optional[bool] = Field(default=None,alias="isSearchEngineIndexabilityDisabled",)
	isTimeSlotTimeZoneSetToBusinessTimeZone: Optional[bool] = Field(default=None,alias="isTimeSlotTimeZoneSetToBusinessTimeZone",)
	privacyPolicyWebUrl: Optional[str] = Field(default=None,alias="privacyPolicyWebUrl",)
	termsAndConditionsWebUrl: Optional[str] = Field(default=None,alias="termsAndConditionsWebUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .booking_page_access_control import BookingPageAccessControl

