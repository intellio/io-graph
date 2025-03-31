from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsFirewallNetworkProfile(BaseModel):
	authorizedApplicationRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="authorizedApplicationRulesFromGroupPolicyMerged", default=None,)
	connectionSecurityRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="connectionSecurityRulesFromGroupPolicyMerged", default=None,)
	firewallEnabled: Optional[StateManagementSetting | str] = Field(alias="firewallEnabled", default=None,)
	globalPortRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="globalPortRulesFromGroupPolicyMerged", default=None,)
	inboundConnectionsBlocked: Optional[bool] = Field(alias="inboundConnectionsBlocked", default=None,)
	inboundNotificationsBlocked: Optional[bool] = Field(alias="inboundNotificationsBlocked", default=None,)
	incomingTrafficBlocked: Optional[bool] = Field(alias="incomingTrafficBlocked", default=None,)
	outboundConnectionsBlocked: Optional[bool] = Field(alias="outboundConnectionsBlocked", default=None,)
	policyRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="policyRulesFromGroupPolicyMerged", default=None,)
	securedPacketExemptionAllowed: Optional[bool] = Field(alias="securedPacketExemptionAllowed", default=None,)
	stealthModeBlocked: Optional[bool] = Field(alias="stealthModeBlocked", default=None,)
	unicastResponsesToMulticastBroadcastsBlocked: Optional[bool] = Field(alias="unicastResponsesToMulticastBroadcastsBlocked", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .state_management_setting import StateManagementSetting
