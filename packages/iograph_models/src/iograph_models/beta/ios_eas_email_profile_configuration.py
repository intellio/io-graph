from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class IosEasEmailProfileConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.iosEasEmailProfileConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.iosEasEmailProfileConfiguration")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceManagementApplicabilityRuleDeviceMode: Optional[DeviceManagementApplicabilityRuleDeviceMode] = Field(alias="deviceManagementApplicabilityRuleDeviceMode", default=None,)
	deviceManagementApplicabilityRuleOsEdition: Optional[DeviceManagementApplicabilityRuleOsEdition] = Field(alias="deviceManagementApplicabilityRuleOsEdition", default=None,)
	deviceManagementApplicabilityRuleOsVersion: Optional[DeviceManagementApplicabilityRuleOsVersion] = Field(alias="deviceManagementApplicabilityRuleOsVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supportsScopeTags: Optional[bool] = Field(alias="supportsScopeTags", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceConfigurationAssignment]] = Field(alias="assignments", default=None,)
	deviceSettingStateSummaries: Optional[list[SettingStateDeviceSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStatuses: Optional[list[DeviceConfigurationDeviceStatus]] = Field(alias="deviceStatuses", default=None,)
	deviceStatusOverview: Optional[DeviceConfigurationDeviceOverview] = Field(alias="deviceStatusOverview", default=None,)
	groupAssignments: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="groupAssignments", default=None,)
	userStatuses: Optional[list[DeviceConfigurationUserStatus]] = Field(alias="userStatuses", default=None,)
	userStatusOverview: Optional[DeviceConfigurationUserOverview] = Field(alias="userStatusOverview", default=None,)
	customDomainName: Optional[str] = Field(alias="customDomainName", default=None,)
	userDomainNameSource: Optional[DomainNameSource | str] = Field(alias="userDomainNameSource", default=None,)
	usernameAADSource: Optional[UsernameSource | str] = Field(alias="usernameAADSource", default=None,)
	usernameSource: Optional[UserEmailSource | str] = Field(alias="usernameSource", default=None,)
	accountName: Optional[str] = Field(alias="accountName", default=None,)
	authenticationMethod: Optional[EasAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	blockMovingMessagesToOtherEmailAccounts: Optional[bool] = Field(alias="blockMovingMessagesToOtherEmailAccounts", default=None,)
	blockSendingEmailFromThirdPartyApps: Optional[bool] = Field(alias="blockSendingEmailFromThirdPartyApps", default=None,)
	blockSyncingRecentlyUsedEmailAddresses: Optional[bool] = Field(alias="blockSyncingRecentlyUsedEmailAddresses", default=None,)
	durationOfEmailToSync: Optional[EmailSyncDuration | str] = Field(alias="durationOfEmailToSync", default=None,)
	easServices: Optional[EasServices | str] = Field(alias="easServices", default=None,)
	easServicesUserOverrideEnabled: Optional[bool] = Field(alias="easServicesUserOverrideEnabled", default=None,)
	emailAddressSource: Optional[UserEmailSource | str] = Field(alias="emailAddressSource", default=None,)
	encryptionCertificateType: Optional[EmailCertificateType | str] = Field(alias="encryptionCertificateType", default=None,)
	hostName: Optional[str] = Field(alias="hostName", default=None,)
	perAppVPNProfileId: Optional[str] = Field(alias="perAppVPNProfileId", default=None,)
	requireSmime: Optional[bool] = Field(alias="requireSmime", default=None,)
	requireSsl: Optional[bool] = Field(alias="requireSsl", default=None,)
	signingCertificateType: Optional[EmailCertificateType | str] = Field(alias="signingCertificateType", default=None,)
	smimeEnablePerMessageSwitch: Optional[bool] = Field(alias="smimeEnablePerMessageSwitch", default=None,)
	smimeEncryptByDefaultEnabled: Optional[bool] = Field(alias="smimeEncryptByDefaultEnabled", default=None,)
	smimeEncryptByDefaultUserOverrideEnabled: Optional[bool] = Field(alias="smimeEncryptByDefaultUserOverrideEnabled", default=None,)
	smimeEncryptionCertificateUserOverrideEnabled: Optional[bool] = Field(alias="smimeEncryptionCertificateUserOverrideEnabled", default=None,)
	smimeSigningCertificateUserOverrideEnabled: Optional[bool] = Field(alias="smimeSigningCertificateUserOverrideEnabled", default=None,)
	smimeSigningEnabled: Optional[bool] = Field(alias="smimeSigningEnabled", default=None,)
	smimeSigningUserOverrideEnabled: Optional[bool] = Field(alias="smimeSigningUserOverrideEnabled", default=None,)
	useOAuth: Optional[bool] = Field(alias="useOAuth", default=None,)
	derivedCredentialSettings: Optional[DeviceManagementDerivedCredentialSettings] = Field(alias="derivedCredentialSettings", default=None,)
	identityCertificate: Optional[Union[IosPkcsCertificateProfile, IosScepCertificateProfile]] = Field(alias="identityCertificate", default=None,discriminator="odata_type", )
	smimeEncryptionCertificate: Optional[Union[IosPkcsCertificateProfile, IosScepCertificateProfile, IosImportedPFXCertificateProfile]] = Field(alias="smimeEncryptionCertificate", default=None,discriminator="odata_type", )
	smimeSigningCertificate: Optional[Union[IosPkcsCertificateProfile, IosScepCertificateProfile, IosImportedPFXCertificateProfile]] = Field(alias="smimeSigningCertificate", default=None,discriminator="odata_type", )

from .device_management_applicability_rule_device_mode import DeviceManagementApplicabilityRuleDeviceMode
from .device_management_applicability_rule_os_edition import DeviceManagementApplicabilityRuleOsEdition
from .device_management_applicability_rule_os_version import DeviceManagementApplicabilityRuleOsVersion
from .device_configuration_assignment import DeviceConfigurationAssignment
from .setting_state_device_summary import SettingStateDeviceSummary
from .device_configuration_device_status import DeviceConfigurationDeviceStatus
from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
from .device_configuration_user_status import DeviceConfigurationUserStatus
from .device_configuration_user_overview import DeviceConfigurationUserOverview
from .domain_name_source import DomainNameSource
from .username_source import UsernameSource
from .user_email_source import UserEmailSource
from .eas_authentication_method import EasAuthenticationMethod
from .email_sync_duration import EmailSyncDuration
from .eas_services import EasServices
from .email_certificate_type import EmailCertificateType
from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
from .ios_pkcs_certificate_profile import IosPkcsCertificateProfile
from .ios_scep_certificate_profile import IosScepCertificateProfile
from .ios_imported_p_f_x_certificate_profile import IosImportedPFXCertificateProfile
