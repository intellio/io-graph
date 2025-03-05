from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsFirewallNetworkProfile(BaseModel):
	authorizedApplicationRulesFromGroupPolicyMerged: Optional[bool] = Field(default=None,alias="authorizedApplicationRulesFromGroupPolicyMerged",)
	connectionSecurityRulesFromGroupPolicyMerged: Optional[bool] = Field(default=None,alias="connectionSecurityRulesFromGroupPolicyMerged",)
	firewallEnabled: Optional[StateManagementSetting] = Field(default=None,alias="firewallEnabled",)
	globalPortRulesFromGroupPolicyMerged: Optional[bool] = Field(default=None,alias="globalPortRulesFromGroupPolicyMerged",)
	inboundConnectionsBlocked: Optional[bool] = Field(default=None,alias="inboundConnectionsBlocked",)
	inboundNotificationsBlocked: Optional[bool] = Field(default=None,alias="inboundNotificationsBlocked",)
	incomingTrafficBlocked: Optional[bool] = Field(default=None,alias="incomingTrafficBlocked",)
	outboundConnectionsBlocked: Optional[bool] = Field(default=None,alias="outboundConnectionsBlocked",)
	policyRulesFromGroupPolicyMerged: Optional[bool] = Field(default=None,alias="policyRulesFromGroupPolicyMerged",)
	securedPacketExemptionAllowed: Optional[bool] = Field(default=None,alias="securedPacketExemptionAllowed",)
	stealthModeBlocked: Optional[bool] = Field(default=None,alias="stealthModeBlocked",)
	unicastResponsesToMulticastBroadcastsBlocked: Optional[bool] = Field(default=None,alias="unicastResponsesToMulticastBroadcastsBlocked",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .state_management_setting import StateManagementSetting

