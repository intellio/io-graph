from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class Windows10VpnConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10VpnConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windows10VpnConfiguration")
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
	connectionName: Optional[str] = Field(alias="connectionName", default=None,)
	customXml: Optional[str] = Field(alias="customXml", default=None,)
	servers: Optional[list[VpnServer]] = Field(alias="servers", default=None,)
	associatedApps: Optional[list[Windows10AssociatedApps]] = Field(alias="associatedApps", default=None,)
	authenticationMethod: Optional[Windows10VpnAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	connectionType: Optional[Windows10VpnConnectionType | str] = Field(alias="connectionType", default=None,)
	cryptographySuite: Optional[CryptographySuite] = Field(alias="cryptographySuite", default=None,)
	dnsRules: Optional[list[VpnDnsRule]] = Field(alias="dnsRules", default=None,)
	dnsSuffixes: Optional[list[str]] = Field(alias="dnsSuffixes", default=None,)
	eapXml: Optional[str] = Field(alias="eapXml", default=None,)
	enableAlwaysOn: Optional[bool] = Field(alias="enableAlwaysOn", default=None,)
	enableConditionalAccess: Optional[bool] = Field(alias="enableConditionalAccess", default=None,)
	enableDeviceTunnel: Optional[bool] = Field(alias="enableDeviceTunnel", default=None,)
	enableDnsRegistration: Optional[bool] = Field(alias="enableDnsRegistration", default=None,)
	enableSingleSignOnWithAlternateCertificate: Optional[bool] = Field(alias="enableSingleSignOnWithAlternateCertificate", default=None,)
	enableSplitTunneling: Optional[bool] = Field(alias="enableSplitTunneling", default=None,)
	microsoftTunnelSiteId: Optional[str] = Field(alias="microsoftTunnelSiteId", default=None,)
	onlyAssociatedAppsCanUseConnection: Optional[bool] = Field(alias="onlyAssociatedAppsCanUseConnection", default=None,)
	profileTarget: Optional[Windows10VpnProfileTarget | str] = Field(alias="profileTarget", default=None,)
	proxyServer: Optional[Windows10VpnProxyServer] = Field(alias="proxyServer", default=None,)
	rememberUserCredentials: Optional[bool] = Field(alias="rememberUserCredentials", default=None,)
	routes: Optional[list[VpnRoute]] = Field(alias="routes", default=None,)
	singleSignOnEku: Optional[ExtendedKeyUsage] = Field(alias="singleSignOnEku", default=None,)
	singleSignOnIssuerHash: Optional[str] = Field(alias="singleSignOnIssuerHash", default=None,)
	trafficRules: Optional[list[VpnTrafficRule]] = Field(alias="trafficRules", default=None,)
	trustedNetworkDomains: Optional[list[str]] = Field(alias="trustedNetworkDomains", default=None,)
	windowsInformationProtectionDomain: Optional[str] = Field(alias="windowsInformationProtectionDomain", default=None,)
	identityCertificate: Optional[Union[Windows10PkcsCertificateProfile, Windows10ImportedPFXCertificateProfile, Windows81SCEPCertificateProfile, WindowsPhone81ImportedPFXCertificateProfile]] = Field(alias="identityCertificate", default=None,discriminator="odata_type", )

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
from .vpn_server import VpnServer
from .windows10_associated_apps import Windows10AssociatedApps
from .windows10_vpn_authentication_method import Windows10VpnAuthenticationMethod
from .windows10_vpn_connection_type import Windows10VpnConnectionType
from .cryptography_suite import CryptographySuite
from .vpn_dns_rule import VpnDnsRule
from .windows10_vpn_profile_target import Windows10VpnProfileTarget
from .windows10_vpn_proxy_server import Windows10VpnProxyServer
from .vpn_route import VpnRoute
from .extended_key_usage import ExtendedKeyUsage
from .vpn_traffic_rule import VpnTrafficRule
from .windows10_pkcs_certificate_profile import Windows10PkcsCertificateProfile
from .windows10_imported_p_f_x_certificate_profile import Windows10ImportedPFXCertificateProfile
from .windows81_s_c_e_p_certificate_profile import Windows81SCEPCertificateProfile
from .windows_phone81_imported_p_f_x_certificate_profile import WindowsPhone81ImportedPFXCertificateProfile
