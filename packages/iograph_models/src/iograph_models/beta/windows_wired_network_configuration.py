from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsWiredNetworkConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsWiredNetworkConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsWiredNetworkConfiguration")
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
	authenticationBlockPeriodInMinutes: Optional[int] = Field(alias="authenticationBlockPeriodInMinutes", default=None,)
	authenticationMethod: Optional[WiredNetworkAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	authenticationPeriodInSeconds: Optional[int] = Field(alias="authenticationPeriodInSeconds", default=None,)
	authenticationRetryDelayPeriodInSeconds: Optional[int] = Field(alias="authenticationRetryDelayPeriodInSeconds", default=None,)
	authenticationType: Optional[WiredNetworkAuthenticationType | str] = Field(alias="authenticationType", default=None,)
	cacheCredentials: Optional[bool] = Field(alias="cacheCredentials", default=None,)
	disableUserPromptForServerValidation: Optional[bool] = Field(alias="disableUserPromptForServerValidation", default=None,)
	eapolStartPeriodInSeconds: Optional[int] = Field(alias="eapolStartPeriodInSeconds", default=None,)
	eapType: Optional[EapType | str] = Field(alias="eapType", default=None,)
	enforce8021X: Optional[bool] = Field(alias="enforce8021X", default=None,)
	forceFIPSCompliance: Optional[bool] = Field(alias="forceFIPSCompliance", default=None,)
	innerAuthenticationProtocolForEAPTTLS: Optional[NonEapAuthenticationMethodForEapTtlsType | str] = Field(alias="innerAuthenticationProtocolForEAPTTLS", default=None,)
	maximumAuthenticationFailures: Optional[int] = Field(alias="maximumAuthenticationFailures", default=None,)
	maximumEAPOLStartMessages: Optional[int] = Field(alias="maximumEAPOLStartMessages", default=None,)
	outerIdentityPrivacyTemporaryValue: Optional[str] = Field(alias="outerIdentityPrivacyTemporaryValue", default=None,)
	performServerValidation: Optional[bool] = Field(alias="performServerValidation", default=None,)
	requireCryptographicBinding: Optional[bool] = Field(alias="requireCryptographicBinding", default=None,)
	secondaryAuthenticationMethod: Optional[WiredNetworkAuthenticationMethod | str] = Field(alias="secondaryAuthenticationMethod", default=None,)
	trustedServerCertificateNames: Optional[list[str]] = Field(alias="trustedServerCertificateNames", default=None,)
	identityCertificateForClientAuthentication: Optional[Union[Windows10CertificateProfileBase, Windows10PkcsCertificateProfile, Windows10ImportedPFXCertificateProfile, Windows81CertificateProfileBase, Windows81SCEPCertificateProfile, WindowsPhone81ImportedPFXCertificateProfile]] = Field(alias="identityCertificateForClientAuthentication", default=None,discriminator="odata_type", )
	rootCertificateForClientValidation: Optional[Windows81TrustedRootCertificate] = Field(alias="rootCertificateForClientValidation", default=None,)
	rootCertificatesForServerValidation: Optional[list[Windows81TrustedRootCertificate]] = Field(alias="rootCertificatesForServerValidation", default=None,)
	secondaryIdentityCertificateForClientAuthentication: Optional[Union[Windows10CertificateProfileBase, Windows10PkcsCertificateProfile, Windows10ImportedPFXCertificateProfile, Windows81CertificateProfileBase, Windows81SCEPCertificateProfile, WindowsPhone81ImportedPFXCertificateProfile]] = Field(alias="secondaryIdentityCertificateForClientAuthentication", default=None,discriminator="odata_type", )
	secondaryRootCertificateForClientValidation: Optional[Windows81TrustedRootCertificate] = Field(alias="secondaryRootCertificateForClientValidation", default=None,)

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
from .wired_network_authentication_method import WiredNetworkAuthenticationMethod
from .wired_network_authentication_type import WiredNetworkAuthenticationType
from .eap_type import EapType
from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
from .wired_network_authentication_method import WiredNetworkAuthenticationMethod
from .windows10_certificate_profile_base import Windows10CertificateProfileBase
from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
from .windows81_certificate_profile_base import Windows81CertificateProfileBase
from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
from .windows10_certificate_profile_base import Windows10CertificateProfileBase
from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
from .windows81_certificate_profile_base import Windows81CertificateProfileBase
from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate

