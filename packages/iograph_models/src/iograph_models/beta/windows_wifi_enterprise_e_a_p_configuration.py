from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsWifiEnterpriseEAPConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsWifiEnterpriseEAPConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsWifiEnterpriseEAPConfiguration")
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
	connectAutomatically: Optional[bool] = Field(alias="connectAutomatically", default=None,)
	connectToPreferredNetwork: Optional[bool] = Field(alias="connectToPreferredNetwork", default=None,)
	connectWhenNetworkNameIsHidden: Optional[bool] = Field(alias="connectWhenNetworkNameIsHidden", default=None,)
	forceFIPSCompliance: Optional[bool] = Field(alias="forceFIPSCompliance", default=None,)
	meteredConnectionLimit: Optional[MeteredConnectionLimitType | str] = Field(alias="meteredConnectionLimit", default=None,)
	networkName: Optional[str] = Field(alias="networkName", default=None,)
	preSharedKey: Optional[str] = Field(alias="preSharedKey", default=None,)
	proxyAutomaticConfigurationUrl: Optional[str] = Field(alias="proxyAutomaticConfigurationUrl", default=None,)
	proxyManualAddress: Optional[str] = Field(alias="proxyManualAddress", default=None,)
	proxyManualPort: Optional[int] = Field(alias="proxyManualPort", default=None,)
	proxySetting: Optional[WiFiProxySetting | str] = Field(alias="proxySetting", default=None,)
	ssid: Optional[str] = Field(alias="ssid", default=None,)
	wifiSecurityType: Optional[WiFiSecurityType | str] = Field(alias="wifiSecurityType", default=None,)
	authenticationMethod: Optional[WiFiAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	authenticationPeriodInSeconds: Optional[int] = Field(alias="authenticationPeriodInSeconds", default=None,)
	authenticationRetryDelayPeriodInSeconds: Optional[int] = Field(alias="authenticationRetryDelayPeriodInSeconds", default=None,)
	authenticationType: Optional[WifiAuthenticationType | str] = Field(alias="authenticationType", default=None,)
	cacheCredentials: Optional[bool] = Field(alias="cacheCredentials", default=None,)
	disableUserPromptForServerValidation: Optional[bool] = Field(alias="disableUserPromptForServerValidation", default=None,)
	eapolStartPeriodInSeconds: Optional[int] = Field(alias="eapolStartPeriodInSeconds", default=None,)
	eapType: Optional[EapType | str] = Field(alias="eapType", default=None,)
	enablePairwiseMasterKeyCaching: Optional[bool] = Field(alias="enablePairwiseMasterKeyCaching", default=None,)
	enablePreAuthentication: Optional[bool] = Field(alias="enablePreAuthentication", default=None,)
	innerAuthenticationProtocolForEAPTTLS: Optional[NonEapAuthenticationMethodForEapTtlsType | str] = Field(alias="innerAuthenticationProtocolForEAPTTLS", default=None,)
	maximumAuthenticationFailures: Optional[int] = Field(alias="maximumAuthenticationFailures", default=None,)
	maximumAuthenticationTimeoutInSeconds: Optional[int] = Field(alias="maximumAuthenticationTimeoutInSeconds", default=None,)
	maximumEAPOLStartMessages: Optional[int] = Field(alias="maximumEAPOLStartMessages", default=None,)
	maximumNumberOfPairwiseMasterKeysInCache: Optional[int] = Field(alias="maximumNumberOfPairwiseMasterKeysInCache", default=None,)
	maximumPairwiseMasterKeyCacheTimeInMinutes: Optional[int] = Field(alias="maximumPairwiseMasterKeyCacheTimeInMinutes", default=None,)
	maximumPreAuthenticationAttempts: Optional[int] = Field(alias="maximumPreAuthenticationAttempts", default=None,)
	networkSingleSignOn: Optional[NetworkSingleSignOnType | str] = Field(alias="networkSingleSignOn", default=None,)
	outerIdentityPrivacyTemporaryValue: Optional[str] = Field(alias="outerIdentityPrivacyTemporaryValue", default=None,)
	performServerValidation: Optional[bool] = Field(alias="performServerValidation", default=None,)
	promptForAdditionalAuthenticationCredentials: Optional[bool] = Field(alias="promptForAdditionalAuthenticationCredentials", default=None,)
	requireCryptographicBinding: Optional[bool] = Field(alias="requireCryptographicBinding", default=None,)
	trustedServerCertificateNames: Optional[list[str]] = Field(alias="trustedServerCertificateNames", default=None,)
	userBasedVirtualLan: Optional[bool] = Field(alias="userBasedVirtualLan", default=None,)
	identityCertificateForClientAuthentication: Optional[Union[Windows10PkcsCertificateProfile, Windows10ImportedPFXCertificateProfile, Windows81SCEPCertificateProfile, WindowsPhone81ImportedPFXCertificateProfile]] = Field(alias="identityCertificateForClientAuthentication", default=None,discriminator="odata_type", )
	rootCertificateForClientValidation: Optional[Windows81TrustedRootCertificate] = Field(alias="rootCertificateForClientValidation", default=None,)
	rootCertificatesForServerValidation: Optional[list[Windows81TrustedRootCertificate]] = Field(alias="rootCertificatesForServerValidation", default=None,)

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
from .metered_connection_limit_type import MeteredConnectionLimitType
from .wi_fi_proxy_setting import WiFiProxySetting
from .wi_fi_security_type import WiFiSecurityType
from .wi_fi_authentication_method import WiFiAuthenticationMethod
from .wifi_authentication_type import WifiAuthenticationType
from .eap_type import EapType
from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
from .network_single_sign_on_type import NetworkSingleSignOnType
from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
from .windows81_trusted_root_certificate import Windows81TrustedRootCertificate
