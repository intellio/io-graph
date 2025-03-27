from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DepEnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.depEnrollmentProfile"] = Field(alias="@odata.type", default="#microsoft.graph.depEnrollmentProfile")
	configurationEndpointUrl: Optional[str] = Field(alias="configurationEndpointUrl", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enableAuthenticationViaCompanyPortal: Optional[bool] = Field(alias="enableAuthenticationViaCompanyPortal", default=None,)
	requireCompanyPortalOnSetupAssistantEnrolledDevices: Optional[bool] = Field(alias="requireCompanyPortalOnSetupAssistantEnrolledDevices", default=None,)
	requiresUserAuthentication: Optional[bool] = Field(alias="requiresUserAuthentication", default=None,)
	appleIdDisabled: Optional[bool] = Field(alias="appleIdDisabled", default=None,)
	applePayDisabled: Optional[bool] = Field(alias="applePayDisabled", default=None,)
	awaitDeviceConfiguredConfirmation: Optional[bool] = Field(alias="awaitDeviceConfiguredConfirmation", default=None,)
	diagnosticsDisabled: Optional[bool] = Field(alias="diagnosticsDisabled", default=None,)
	enableSharedIPad: Optional[bool] = Field(alias="enableSharedIPad", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isMandatory: Optional[bool] = Field(alias="isMandatory", default=None,)
	iTunesPairingMode: Optional[ITunesPairingMode | str] = Field(alias="iTunesPairingMode", default=None,)
	locationDisabled: Optional[bool] = Field(alias="locationDisabled", default=None,)
	macOSFileVaultDisabled: Optional[bool] = Field(alias="macOSFileVaultDisabled", default=None,)
	macOSRegistrationDisabled: Optional[bool] = Field(alias="macOSRegistrationDisabled", default=None,)
	managementCertificates: Optional[list[ManagementCertificateWithThumbprint]] = Field(alias="managementCertificates", default=None,)
	passCodeDisabled: Optional[bool] = Field(alias="passCodeDisabled", default=None,)
	profileRemovalDisabled: Optional[bool] = Field(alias="profileRemovalDisabled", default=None,)
	restoreBlocked: Optional[bool] = Field(alias="restoreBlocked", default=None,)
	restoreFromAndroidDisabled: Optional[bool] = Field(alias="restoreFromAndroidDisabled", default=None,)
	sharedIPadMaximumUserCount: Optional[int] = Field(alias="sharedIPadMaximumUserCount", default=None,)
	siriDisabled: Optional[bool] = Field(alias="siriDisabled", default=None,)
	supervisedModeEnabled: Optional[bool] = Field(alias="supervisedModeEnabled", default=None,)
	supportDepartment: Optional[str] = Field(alias="supportDepartment", default=None,)
	supportPhoneNumber: Optional[str] = Field(alias="supportPhoneNumber", default=None,)
	termsAndConditionsDisabled: Optional[bool] = Field(alias="termsAndConditionsDisabled", default=None,)
	touchIdDisabled: Optional[bool] = Field(alias="touchIdDisabled", default=None,)
	zoomDisabled: Optional[bool] = Field(alias="zoomDisabled", default=None,)

from .i_tunes_pairing_mode import ITunesPairingMode
from .management_certificate_with_thumbprint import ManagementCertificateWithThumbprint

