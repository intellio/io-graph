from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AppleVpnConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appleVpnConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.appleVpnConfiguration")
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
	associatedDomains: Optional[list[str]] = Field(alias="associatedDomains", default=None,)
	authenticationMethod: Optional[VpnAuthenticationMethod | str] = Field(alias="authenticationMethod", default=None,)
	connectionName: Optional[str] = Field(alias="connectionName", default=None,)
	connectionType: Optional[AppleVpnConnectionType | str] = Field(alias="connectionType", default=None,)
	customData: Optional[list[KeyValue]] = Field(alias="customData", default=None,)
	customKeyValueData: Optional[list[KeyValuePair]] = Field(alias="customKeyValueData", default=None,)
	disableOnDemandUserOverride: Optional[bool] = Field(alias="disableOnDemandUserOverride", default=None,)
	disconnectOnIdle: Optional[bool] = Field(alias="disconnectOnIdle", default=None,)
	disconnectOnIdleTimerInSeconds: Optional[int] = Field(alias="disconnectOnIdleTimerInSeconds", default=None,)
	enablePerApp: Optional[bool] = Field(alias="enablePerApp", default=None,)
	enableSplitTunneling: Optional[bool] = Field(alias="enableSplitTunneling", default=None,)
	excludedDomains: Optional[list[str]] = Field(alias="excludedDomains", default=None,)
	identifier: Optional[str] = Field(alias="identifier", default=None,)
	loginGroupOrDomain: Optional[str] = Field(alias="loginGroupOrDomain", default=None,)
	onDemandRules: Optional[list[VpnOnDemandRule]] = Field(alias="onDemandRules", default=None,)
	optInToDeviceIdSharing: Optional[bool] = Field(alias="optInToDeviceIdSharing", default=None,)
	providerType: Optional[VpnProviderType | str] = Field(alias="providerType", default=None,)
	proxyServer: Optional[Union[Windows10VpnProxyServer, Windows81VpnProxyServer]] = Field(alias="proxyServer", default=None,discriminator="odata_type", )
	realm: Optional[str] = Field(alias="realm", default=None,)
	role: Optional[str] = Field(alias="role", default=None,)
	safariDomains: Optional[list[str]] = Field(alias="safariDomains", default=None,)
	server: Optional[VpnServer] = Field(alias="server", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.iosVpnConfiguration":
				from .ios_vpn_configuration import IosVpnConfiguration
				return IosVpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.iosikEv2VpnConfiguration":
				from .iosik_ev2_vpn_configuration import IosikEv2VpnConfiguration
				return IosikEv2VpnConfiguration.model_validate(data)
			if mapping_key == "#microsoft.graph.macOSVpnConfiguration":
				from .mac_o_s_vpn_configuration import MacOSVpnConfiguration
				return MacOSVpnConfiguration.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

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
from .apple_vpn_connection_type import AppleVpnConnectionType
from .key_value import KeyValue
from .key_value_pair import KeyValuePair
from .vpn_on_demand_rule import VpnOnDemandRule
from .vpn_provider_type import VpnProviderType
from .windows10_vpn_proxy_server import Windows10VpnProxyServer
from .windows81_vpn_proxy_server import Windows81VpnProxyServer
from .vpn_server import VpnServer

