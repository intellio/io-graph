from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class AndroidDeviceOwnerVpnConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidDeviceOwnerVpnConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceOwnerVpnConfiguration")
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
	authenticationMethod: Optional[VpnAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	connectionName: Optional[str] = Field(alias="connectionName", default=None,)
	realm: Optional[str] = Field(alias="realm", default=None,)
	role: Optional[str] = Field(alias="role", default=None,)
	servers: Optional[list[VpnServer]] = Field(alias="servers", default=None,)
	alwaysOn: Optional[bool] = Field(alias="alwaysOn", default=None,)
	alwaysOnLockdown: Optional[bool] = Field(alias="alwaysOnLockdown", default=None,)
	connectionType: Optional[AndroidVpnConnectionType | str] = Field(alias="connectionType", default=None,)
	customData: Optional[list[KeyValue]] = Field(alias="customData", default=None,)
	customKeyValueData: Optional[list[KeyValuePair]] = Field(alias="customKeyValueData", default=None,)
	microsoftTunnelSiteId: Optional[str] = Field(alias="microsoftTunnelSiteId", default=None,)
	proxyExclusionList: Optional[list[str]] = Field(alias="proxyExclusionList", default=None,)
	proxyServer: Optional[Union[Windows10VpnProxyServer, Windows81VpnProxyServer]] = Field(alias="proxyServer", default=None,discriminator="odata_type", )
	targetedMobileApps: Optional[list[Annotated[Union[AppleAppListItem],Field(discriminator="odata_type")]]] = Field(alias="targetedMobileApps", default=None,)
	targetedPackageIds: Optional[list[str]] = Field(alias="targetedPackageIds", default=None,)
	derivedCredentialSettings: Optional[DeviceManagementDerivedCredentialSettings] = Field(alias="derivedCredentialSettings", default=None,)
	identityCertificate: Optional[Union[AndroidDeviceOwnerImportedPFXCertificateProfile, AndroidDeviceOwnerPkcsCertificateProfile, AndroidDeviceOwnerScepCertificateProfile]] = Field(alias="identityCertificate", default=None,discriminator="odata_type", )

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
from .vpn_authentication_method import VpnAuthenticationMethod
from .vpn_server import VpnServer
from .android_vpn_connection_type import AndroidVpnConnectionType
from .key_value import KeyValue
from .key_value_pair import KeyValuePair
from .windows10_vpn_proxy_server import Windows10VpnProxyServer
from .windows81_vpn_proxy_server import Windows81VpnProxyServer
from .apple_app_list_item import AppleAppListItem
from .device_management_derived_credential_settings import DeviceManagementDerivedCredentialSettings
from .android_device_owner_imported_p_f_x_certificate_profile import AndroidDeviceOwnerImportedPFXCertificateProfile
from .android_device_owner_pkcs_certificate_profile import AndroidDeviceOwnerPkcsCertificateProfile
from .android_device_owner_scep_certificate_profile import AndroidDeviceOwnerScepCertificateProfile
