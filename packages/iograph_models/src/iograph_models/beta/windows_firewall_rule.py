from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsFirewallRule(BaseModel):
	action: Optional[StateManagementSetting | str] = Field(alias="action", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	edgeTraversal: Optional[StateManagementSetting | str] = Field(alias="edgeTraversal", default=None,)
	filePath: Optional[str] = Field(alias="filePath", default=None,)
	interfaceTypes: Optional[WindowsFirewallRuleInterfaceTypes | str] = Field(alias="interfaceTypes", default=None,)
	localAddressRanges: Optional[list[str]] = Field(alias="localAddressRanges", default=None,)
	localPortRanges: Optional[list[str]] = Field(alias="localPortRanges", default=None,)
	localUserAuthorizations: Optional[str] = Field(alias="localUserAuthorizations", default=None,)
	packageFamilyName: Optional[str] = Field(alias="packageFamilyName", default=None,)
	profileTypes: Optional[WindowsFirewallRuleNetworkProfileTypes | str] = Field(alias="profileTypes", default=None,)
	protocol: Optional[int] = Field(alias="protocol", default=None,)
	remoteAddressRanges: Optional[list[str]] = Field(alias="remoteAddressRanges", default=None,)
	remotePortRanges: Optional[list[str]] = Field(alias="remotePortRanges", default=None,)
	serviceName: Optional[str] = Field(alias="serviceName", default=None,)
	trafficDirection: Optional[WindowsFirewallRuleTrafficDirectionType | str] = Field(alias="trafficDirection", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .state_management_setting import StateManagementSetting
from .windows_firewall_rule_interface_types import WindowsFirewallRuleInterfaceTypes
from .windows_firewall_rule_network_profile_types import WindowsFirewallRuleNetworkProfileTypes
from .windows_firewall_rule_traffic_direction_type import WindowsFirewallRuleTrafficDirectionType
