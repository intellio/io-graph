from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSEnterpriseWiFiConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSEnterpriseWiFiConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.macOSEnterpriseWiFiConfiguration")
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
	connectWhenNetworkNameIsHidden: Optional[bool] = Field(alias="connectWhenNetworkNameIsHidden", default=None,)
	deploymentChannel: Optional[AppleDeploymentChannel | str] = Field(alias="deploymentChannel", default=None,)
	networkName: Optional[str] = Field(alias="networkName", default=None,)
	preSharedKey: Optional[str] = Field(alias="preSharedKey", default=None,)
	proxyAutomaticConfigurationUrl: Optional[str] = Field(alias="proxyAutomaticConfigurationUrl", default=None,)
	proxyManualAddress: Optional[str] = Field(alias="proxyManualAddress", default=None,)
	proxyManualPort: Optional[int] = Field(alias="proxyManualPort", default=None,)
	proxySettings: Optional[WiFiProxySetting | str] = Field(alias="proxySettings", default=None,)
	ssid: Optional[str] = Field(alias="ssid", default=None,)
	wiFiSecurityType: Optional[WiFiSecurityType | str] = Field(alias="wiFiSecurityType", default=None,)
	authenticationMethod: Optional[WiFiAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	eapFastConfiguration: Optional[EapFastConfiguration | str] = Field(alias="eapFastConfiguration", default=None,)
	eapType: Optional[EapType | str] = Field(alias="eapType", default=None,)
	innerAuthenticationProtocolForEapTtls: Optional[NonEapAuthenticationMethodForEapTtlsType | str] = Field(alias="innerAuthenticationProtocolForEapTtls", default=None,)
	outerIdentityPrivacyTemporaryValue: Optional[str] = Field(alias="outerIdentityPrivacyTemporaryValue", default=None,)
	trustedServerCertificateNames: Optional[list[str]] = Field(alias="trustedServerCertificateNames", default=None,)
	identityCertificateForClientAuthentication: Optional[Union[MacOSImportedPFXCertificateProfile, MacOSPkcsCertificateProfile, MacOSScepCertificateProfile]] = Field(alias="identityCertificateForClientAuthentication", default=None,discriminator="odata_type", )
	rootCertificateForServerValidation: Optional[MacOSTrustedRootCertificate] = Field(alias="rootCertificateForServerValidation", default=None,)
	rootCertificatesForServerValidation: Optional[list[MacOSTrustedRootCertificate]] = Field(alias="rootCertificatesForServerValidation", default=None,)

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
from .apple_deployment_channel import AppleDeploymentChannel
from .wi_fi_proxy_setting import WiFiProxySetting
from .wi_fi_security_type import WiFiSecurityType
from .wi_fi_authentication_method import WiFiAuthenticationMethod
from .eap_fast_configuration import EapFastConfiguration
from .eap_type import EapType
from .non_eap_authentication_method_for_eap_ttls_type import NonEapAuthenticationMethodForEapTtlsType
from .mac_o_s_imported_p_f_x_certificate_profile import MacOSImportedPFXCertificateProfile
from .mac_o_s_pkcs_certificate_profile import MacOSPkcsCertificateProfile
from .mac_o_s_scep_certificate_profile import MacOSScepCertificateProfile
from .mac_o_s_trusted_root_certificate import MacOSTrustedRootCertificate
