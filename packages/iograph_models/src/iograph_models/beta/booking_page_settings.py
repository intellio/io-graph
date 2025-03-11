from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BookingPageSettings(BaseModel):
	accessControl: Optional[BookingPageAccessControl | str] = Field(alias="accessControl",default=None,)
	bookingPageColorCode: Optional[str] = Field(alias="bookingPageColorCode",default=None,)
	businessTimeZone: Optional[str] = Field(alias="businessTimeZone",default=None,)
	customerConsentMessage: Optional[str] = Field(alias="customerConsentMessage",default=None,)
	enforceOneTimePassword: Optional[bool] = Field(alias="enforceOneTimePassword",default=None,)
	isBusinessLogoDisplayEnabled: Optional[bool] = Field(alias="isBusinessLogoDisplayEnabled",default=None,)
	isCustomerConsentEnabled: Optional[bool] = Field(alias="isCustomerConsentEnabled",default=None,)
	isSearchEngineIndexabilityDisabled: Optional[bool] = Field(alias="isSearchEngineIndexabilityDisabled",default=None,)
	isTimeSlotTimeZoneSetToBusinessTimeZone: Optional[bool] = Field(alias="isTimeSlotTimeZoneSetToBusinessTimeZone",default=None,)
	privacyPolicyWebUrl: Optional[str] = Field(alias="privacyPolicyWebUrl",default=None,)
	termsAndConditionsWebUrl: Optional[str] = Field(alias="termsAndConditionsWebUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .booking_page_access_control import BookingPageAccessControl

