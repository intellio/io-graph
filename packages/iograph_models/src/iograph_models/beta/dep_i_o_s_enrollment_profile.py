from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DepIOSEnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.depIOSEnrollmentProfile"] = Field(alias="@odata.type", default="#microsoft.graph.depIOSEnrollmentProfile")
	configurationEndpointUrl: Optional[str] = Field(alias="configurationEndpointUrl", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enableAuthenticationViaCompanyPortal: Optional[bool] = Field(alias="enableAuthenticationViaCompanyPortal", default=None,)
	requireCompanyPortalOnSetupAssistantEnrolledDevices: Optional[bool] = Field(alias="requireCompanyPortalOnSetupAssistantEnrolledDevices", default=None,)
	requiresUserAuthentication: Optional[bool] = Field(alias="requiresUserAuthentication", default=None,)
	appleIdDisabled: Optional[bool] = Field(alias="appleIdDisabled", default=None,)
	applePayDisabled: Optional[bool] = Field(alias="applePayDisabled", default=None,)
	configurationWebUrl: Optional[bool] = Field(alias="configurationWebUrl", default=None,)
	deviceNameTemplate: Optional[str] = Field(alias="deviceNameTemplate", default=None,)
	diagnosticsDisabled: Optional[bool] = Field(alias="diagnosticsDisabled", default=None,)
	displayToneSetupDisabled: Optional[bool] = Field(alias="displayToneSetupDisabled", default=None,)
	enabledSkipKeys: Optional[list[str]] = Field(alias="enabledSkipKeys", default=None,)
	enrollmentTimeAzureAdGroupIds: Optional[list[UUID]] = Field(alias="enrollmentTimeAzureAdGroupIds", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isMandatory: Optional[bool] = Field(alias="isMandatory", default=None,)
	locationDisabled: Optional[bool] = Field(alias="locationDisabled", default=None,)
	privacyPaneDisabled: Optional[bool] = Field(alias="privacyPaneDisabled", default=None,)
	profileRemovalDisabled: Optional[bool] = Field(alias="profileRemovalDisabled", default=None,)
	restoreBlocked: Optional[bool] = Field(alias="restoreBlocked", default=None,)
	screenTimeScreenDisabled: Optional[bool] = Field(alias="screenTimeScreenDisabled", default=None,)
	siriDisabled: Optional[bool] = Field(alias="siriDisabled", default=None,)
	supervisedModeEnabled: Optional[bool] = Field(alias="supervisedModeEnabled", default=None,)
	supportDepartment: Optional[str] = Field(alias="supportDepartment", default=None,)
	supportPhoneNumber: Optional[str] = Field(alias="supportPhoneNumber", default=None,)
	termsAndConditionsDisabled: Optional[bool] = Field(alias="termsAndConditionsDisabled", default=None,)
	touchIdDisabled: Optional[bool] = Field(alias="touchIdDisabled", default=None,)
	waitForDeviceConfiguredConfirmation: Optional[bool] = Field(alias="waitForDeviceConfiguredConfirmation", default=None,)
	appearanceScreenDisabled: Optional[bool] = Field(alias="appearanceScreenDisabled", default=None,)
	awaitDeviceConfiguredConfirmation: Optional[bool] = Field(alias="awaitDeviceConfiguredConfirmation", default=None,)
	carrierActivationUrl: Optional[str] = Field(alias="carrierActivationUrl", default=None,)
	companyPortalVppTokenId: Optional[str] = Field(alias="companyPortalVppTokenId", default=None,)
	deviceToDeviceMigrationDisabled: Optional[bool] = Field(alias="deviceToDeviceMigrationDisabled", default=None,)
	enableSharedIPad: Optional[bool] = Field(alias="enableSharedIPad", default=None,)
	enableSingleAppEnrollmentMode: Optional[bool] = Field(alias="enableSingleAppEnrollmentMode", default=None,)
	expressLanguageScreenDisabled: Optional[bool] = Field(alias="expressLanguageScreenDisabled", default=None,)
	forceTemporarySession: Optional[bool] = Field(alias="forceTemporarySession", default=None,)
	homeButtonScreenDisabled: Optional[bool] = Field(alias="homeButtonScreenDisabled", default=None,)
	iMessageAndFaceTimeScreenDisabled: Optional[bool] = Field(alias="iMessageAndFaceTimeScreenDisabled", default=None,)
	iTunesPairingMode: Optional[ITunesPairingMode | str] = Field(alias="iTunesPairingMode", default=None,)
	managementCertificates: Optional[list[ManagementCertificateWithThumbprint]] = Field(alias="managementCertificates", default=None,)
	onBoardingScreenDisabled: Optional[bool] = Field(alias="onBoardingScreenDisabled", default=None,)
	passCodeDisabled: Optional[bool] = Field(alias="passCodeDisabled", default=None,)
	passcodeLockGracePeriodInSeconds: Optional[int] = Field(alias="passcodeLockGracePeriodInSeconds", default=None,)
	preferredLanguageScreenDisabled: Optional[bool] = Field(alias="preferredLanguageScreenDisabled", default=None,)
	restoreCompletedScreenDisabled: Optional[bool] = Field(alias="restoreCompletedScreenDisabled", default=None,)
	restoreFromAndroidDisabled: Optional[bool] = Field(alias="restoreFromAndroidDisabled", default=None,)
	sharedIPadMaximumUserCount: Optional[int] = Field(alias="sharedIPadMaximumUserCount", default=None,)
	simSetupScreenDisabled: Optional[bool] = Field(alias="simSetupScreenDisabled", default=None,)
	softwareUpdateScreenDisabled: Optional[bool] = Field(alias="softwareUpdateScreenDisabled", default=None,)
	temporarySessionTimeoutInSeconds: Optional[int] = Field(alias="temporarySessionTimeoutInSeconds", default=None,)
	updateCompleteScreenDisabled: Optional[bool] = Field(alias="updateCompleteScreenDisabled", default=None,)
	userlessSharedAadModeEnabled: Optional[bool] = Field(alias="userlessSharedAadModeEnabled", default=None,)
	userSessionTimeoutInSeconds: Optional[int] = Field(alias="userSessionTimeoutInSeconds", default=None,)
	watchMigrationScreenDisabled: Optional[bool] = Field(alias="watchMigrationScreenDisabled", default=None,)
	welcomeScreenDisabled: Optional[bool] = Field(alias="welcomeScreenDisabled", default=None,)
	zoomDisabled: Optional[bool] = Field(alias="zoomDisabled", default=None,)

from .i_tunes_pairing_mode import ITunesPairingMode
from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

