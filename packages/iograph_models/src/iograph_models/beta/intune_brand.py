from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IntuneBrand(BaseModel):
	companyPortalBlockedActions: Optional[list[CompanyPortalBlockedAction]] = Field(alias="companyPortalBlockedActions", default=None,)
	contactITEmailAddress: Optional[str] = Field(alias="contactITEmailAddress", default=None,)
	contactITName: Optional[str] = Field(alias="contactITName", default=None,)
	contactITNotes: Optional[str] = Field(alias="contactITNotes", default=None,)
	contactITPhoneNumber: Optional[str] = Field(alias="contactITPhoneNumber", default=None,)
	customCanSeePrivacyMessage: Optional[str] = Field(alias="customCanSeePrivacyMessage", default=None,)
	customCantSeePrivacyMessage: Optional[str] = Field(alias="customCantSeePrivacyMessage", default=None,)
	customPrivacyMessage: Optional[str] = Field(alias="customPrivacyMessage", default=None,)
	darkBackgroundLogo: Optional[MimeContent] = Field(alias="darkBackgroundLogo", default=None,)
	disableClientTelemetry: Optional[bool] = Field(alias="disableClientTelemetry", default=None,)
	disableDeviceCategorySelection: Optional[bool] = Field(alias="disableDeviceCategorySelection", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enrollmentAvailability: Optional[EnrollmentAvailabilityOptions | str] = Field(alias="enrollmentAvailability", default=None,)
	isFactoryResetDisabled: Optional[bool] = Field(alias="isFactoryResetDisabled", default=None,)
	isRemoveDeviceDisabled: Optional[bool] = Field(alias="isRemoveDeviceDisabled", default=None,)
	landingPageCustomizedImage: Optional[MimeContent] = Field(alias="landingPageCustomizedImage", default=None,)
	lightBackgroundLogo: Optional[MimeContent] = Field(alias="lightBackgroundLogo", default=None,)
	onlineSupportSiteName: Optional[str] = Field(alias="onlineSupportSiteName", default=None,)
	onlineSupportSiteUrl: Optional[str] = Field(alias="onlineSupportSiteUrl", default=None,)
	privacyUrl: Optional[str] = Field(alias="privacyUrl", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	sendDeviceOwnershipChangePushNotification: Optional[bool] = Field(alias="sendDeviceOwnershipChangePushNotification", default=None,)
	showAzureADEnterpriseApps: Optional[bool] = Field(alias="showAzureADEnterpriseApps", default=None,)
	showConfigurationManagerApps: Optional[bool] = Field(alias="showConfigurationManagerApps", default=None,)
	showDisplayNameNextToLogo: Optional[bool] = Field(alias="showDisplayNameNextToLogo", default=None,)
	showLogo: Optional[bool] = Field(alias="showLogo", default=None,)
	showNameNextToLogo: Optional[bool] = Field(alias="showNameNextToLogo", default=None,)
	showOfficeWebApps: Optional[bool] = Field(alias="showOfficeWebApps", default=None,)
	themeColor: Optional[RgbColor] = Field(alias="themeColor", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .company_portal_blocked_action import CompanyPortalBlockedAction
from .mime_content import MimeContent
from .enrollment_availability_options import EnrollmentAvailabilityOptions
from .rgb_color import RgbColor
