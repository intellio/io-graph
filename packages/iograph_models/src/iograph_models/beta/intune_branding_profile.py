from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IntuneBrandingProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.intuneBrandingProfile"] = Field(alias="@odata.type", default="#microsoft.graph.intuneBrandingProfile")
	companyPortalBlockedActions: Optional[list[CompanyPortalBlockedAction]] = Field(alias="companyPortalBlockedActions", default=None,)
	contactITEmailAddress: Optional[str] = Field(alias="contactITEmailAddress", default=None,)
	contactITName: Optional[str] = Field(alias="contactITName", default=None,)
	contactITNotes: Optional[str] = Field(alias="contactITNotes", default=None,)
	contactITPhoneNumber: Optional[str] = Field(alias="contactITPhoneNumber", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	customCanSeePrivacyMessage: Optional[str] = Field(alias="customCanSeePrivacyMessage", default=None,)
	customCantSeePrivacyMessage: Optional[str] = Field(alias="customCantSeePrivacyMessage", default=None,)
	customPrivacyMessage: Optional[str] = Field(alias="customPrivacyMessage", default=None,)
	disableClientTelemetry: Optional[bool] = Field(alias="disableClientTelemetry", default=None,)
	disableDeviceCategorySelection: Optional[bool] = Field(alias="disableDeviceCategorySelection", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enrollmentAvailability: Optional[EnrollmentAvailabilityOptions | str] = Field(alias="enrollmentAvailability", default=None,)
	isDefaultProfile: Optional[bool] = Field(alias="isDefaultProfile", default=None,)
	isFactoryResetDisabled: Optional[bool] = Field(alias="isFactoryResetDisabled", default=None,)
	isRemoveDeviceDisabled: Optional[bool] = Field(alias="isRemoveDeviceDisabled", default=None,)
	landingPageCustomizedImage: Optional[MimeContent] = Field(alias="landingPageCustomizedImage", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lightBackgroundLogo: Optional[MimeContent] = Field(alias="lightBackgroundLogo", default=None,)
	onlineSupportSiteName: Optional[str] = Field(alias="onlineSupportSiteName", default=None,)
	onlineSupportSiteUrl: Optional[str] = Field(alias="onlineSupportSiteUrl", default=None,)
	privacyUrl: Optional[str] = Field(alias="privacyUrl", default=None,)
	profileDescription: Optional[str] = Field(alias="profileDescription", default=None,)
	profileName: Optional[str] = Field(alias="profileName", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	sendDeviceOwnershipChangePushNotification: Optional[bool] = Field(alias="sendDeviceOwnershipChangePushNotification", default=None,)
	showAzureADEnterpriseApps: Optional[bool] = Field(alias="showAzureADEnterpriseApps", default=None,)
	showConfigurationManagerApps: Optional[bool] = Field(alias="showConfigurationManagerApps", default=None,)
	showDisplayNameNextToLogo: Optional[bool] = Field(alias="showDisplayNameNextToLogo", default=None,)
	showLogo: Optional[bool] = Field(alias="showLogo", default=None,)
	showOfficeWebApps: Optional[bool] = Field(alias="showOfficeWebApps", default=None,)
	themeColor: Optional[RgbColor] = Field(alias="themeColor", default=None,)
	themeColorLogo: Optional[MimeContent] = Field(alias="themeColorLogo", default=None,)
	assignments: Optional[list[IntuneBrandingProfileAssignment]] = Field(alias="assignments", default=None,)

from .company_portal_blocked_action import CompanyPortalBlockedAction
from .enrollment_availability_options import EnrollmentAvailabilityOptions
from .mime_content import MimeContent
from .rgb_color import RgbColor
from .intune_branding_profile_assignment import IntuneBrandingProfileAssignment
