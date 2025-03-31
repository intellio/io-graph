from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsFirewallNetworkProfile(BaseModel):
	authorizedApplicationRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="authorizedApplicationRulesFromGroupPolicyMerged", default=None,)
	authorizedApplicationRulesFromGroupPolicyNotMerged: Optional[bool] = Field(alias="authorizedApplicationRulesFromGroupPolicyNotMerged", default=None,)
	connectionSecurityRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="connectionSecurityRulesFromGroupPolicyMerged", default=None,)
	connectionSecurityRulesFromGroupPolicyNotMerged: Optional[bool] = Field(alias="connectionSecurityRulesFromGroupPolicyNotMerged", default=None,)
	firewallEnabled: Optional[StateManagementSetting | str] = Field(alias="firewallEnabled", default=None,)
	globalPortRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="globalPortRulesFromGroupPolicyMerged", default=None,)
	globalPortRulesFromGroupPolicyNotMerged: Optional[bool] = Field(alias="globalPortRulesFromGroupPolicyNotMerged", default=None,)
	inboundConnectionsBlocked: Optional[bool] = Field(alias="inboundConnectionsBlocked", default=None,)
	inboundConnectionsRequired: Optional[bool] = Field(alias="inboundConnectionsRequired", default=None,)
	inboundNotificationsBlocked: Optional[bool] = Field(alias="inboundNotificationsBlocked", default=None,)
	inboundNotificationsRequired: Optional[bool] = Field(alias="inboundNotificationsRequired", default=None,)
	incomingTrafficBlocked: Optional[bool] = Field(alias="incomingTrafficBlocked", default=None,)
	incomingTrafficRequired: Optional[bool] = Field(alias="incomingTrafficRequired", default=None,)
	outboundConnectionsBlocked: Optional[bool] = Field(alias="outboundConnectionsBlocked", default=None,)
	outboundConnectionsRequired: Optional[bool] = Field(alias="outboundConnectionsRequired", default=None,)
	policyRulesFromGroupPolicyMerged: Optional[bool] = Field(alias="policyRulesFromGroupPolicyMerged", default=None,)
	policyRulesFromGroupPolicyNotMerged: Optional[bool] = Field(alias="policyRulesFromGroupPolicyNotMerged", default=None,)
	securedPacketExemptionAllowed: Optional[bool] = Field(alias="securedPacketExemptionAllowed", default=None,)
	securedPacketExemptionBlocked: Optional[bool] = Field(alias="securedPacketExemptionBlocked", default=None,)
	stealthModeBlocked: Optional[bool] = Field(alias="stealthModeBlocked", default=None,)
	stealthModeRequired: Optional[bool] = Field(alias="stealthModeRequired", default=None,)
	unicastResponsesToMulticastBroadcastsBlocked: Optional[bool] = Field(alias="unicastResponsesToMulticastBroadcastsBlocked", default=None,)
	unicastResponsesToMulticastBroadcastsRequired: Optional[bool] = Field(alias="unicastResponsesToMulticastBroadcastsRequired", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .state_management_setting import StateManagementSetting
