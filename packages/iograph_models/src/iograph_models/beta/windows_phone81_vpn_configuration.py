from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsPhone81VpnConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsPhone81VpnConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windowsPhone81VpnConfiguration")
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
	applyOnlyToWindows81: Optional[bool] = Field(alias="applyOnlyToWindows81", default=None,)
	connectionType: Optional[WindowsVpnConnectionType | str] = Field(alias="connectionType", default=None,)
	enableSplitTunneling: Optional[bool] = Field(alias="enableSplitTunneling", default=None,)
	loginGroupOrDomain: Optional[str] = Field(alias="loginGroupOrDomain", default=None,)
	proxyServer: Optional[Windows81VpnProxyServer] = Field(alias="proxyServer", default=None,)
	authenticationMethod: Optional[VpnAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	bypassVpnOnCompanyWifi: Optional[bool] = Field(alias="bypassVpnOnCompanyWifi", default=None,)
	bypassVpnOnHomeWifi: Optional[bool] = Field(alias="bypassVpnOnHomeWifi", default=None,)
	dnsSuffixSearchList: Optional[list[str]] = Field(alias="dnsSuffixSearchList", default=None,)
	rememberUserCredentials: Optional[bool] = Field(alias="rememberUserCredentials", default=None,)
	identityCertificate: Optional[Union[WindowsPhone81SCEPCertificateProfile]] = Field(alias="identityCertificate", default=None,discriminator="odata_type", )

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
from .windows_vpn_connection_type import WindowsVpnConnectionType
from .windows81_vpn_proxy_server import Windows81VpnProxyServer
from .vpn_authentication_method import VpnAuthenticationMethod
from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile
