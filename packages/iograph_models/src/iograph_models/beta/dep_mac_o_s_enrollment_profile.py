from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DepMacOSEnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.depMacOSEnrollmentProfile"] = Field(alias="@odata.type", default="#microsoft.graph.depMacOSEnrollmentProfile")
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
	accessibilityScreenDisabled: Optional[bool] = Field(alias="accessibilityScreenDisabled", default=None,)
	adminAccountFullName: Optional[str] = Field(alias="adminAccountFullName", default=None,)
	adminAccountPassword: Optional[str] = Field(alias="adminAccountPassword", default=None,)
	adminAccountUserName: Optional[str] = Field(alias="adminAccountUserName", default=None,)
	autoAdvanceSetupEnabled: Optional[bool] = Field(alias="autoAdvanceSetupEnabled", default=None,)
	autoUnlockWithWatchDisabled: Optional[bool] = Field(alias="autoUnlockWithWatchDisabled", default=None,)
	chooseYourLockScreenDisabled: Optional[bool] = Field(alias="chooseYourLockScreenDisabled", default=None,)
	dontAutoPopulatePrimaryAccountInfo: Optional[bool] = Field(alias="dontAutoPopulatePrimaryAccountInfo", default=None,)
	enableRestrictEditing: Optional[bool] = Field(alias="enableRestrictEditing", default=None,)
	fileVaultDisabled: Optional[bool] = Field(alias="fileVaultDisabled", default=None,)
	hideAdminAccount: Optional[bool] = Field(alias="hideAdminAccount", default=None,)
	iCloudDiagnosticsDisabled: Optional[bool] = Field(alias="iCloudDiagnosticsDisabled", default=None,)
	iCloudStorageDisabled: Optional[bool] = Field(alias="iCloudStorageDisabled", default=None,)
	passCodeDisabled: Optional[bool] = Field(alias="passCodeDisabled", default=None,)
	primaryAccountFullName: Optional[str] = Field(alias="primaryAccountFullName", default=None,)
	primaryAccountUserName: Optional[str] = Field(alias="primaryAccountUserName", default=None,)
	registrationDisabled: Optional[bool] = Field(alias="registrationDisabled", default=None,)
	requestRequiresNetworkTether: Optional[bool] = Field(alias="requestRequiresNetworkTether", default=None,)
	setPrimarySetupAccountAsRegularUser: Optional[bool] = Field(alias="setPrimarySetupAccountAsRegularUser", default=None,)
	skipPrimarySetupAccountCreation: Optional[bool] = Field(alias="skipPrimarySetupAccountCreation", default=None,)
	zoomDisabled: Optional[bool] = Field(alias="zoomDisabled", default=None,)


