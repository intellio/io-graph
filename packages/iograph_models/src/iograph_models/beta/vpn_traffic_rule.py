from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VpnTrafficRule(BaseModel):
	appId: Optional[str] = Field(alias="appId", default=None,)
	appType: Optional[VpnTrafficRuleAppType | str] = Field(alias="appType", default=None,)
	claims: Optional[str] = Field(alias="claims", default=None,)
	localAddressRanges: Optional[list[IPv4Range]] = Field(alias="localAddressRanges", default=None,)
	localPortRanges: Optional[list[NumberRange]] = Field(alias="localPortRanges", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	protocols: Optional[int] = Field(alias="protocols", default=None,)
	remoteAddressRanges: Optional[list[IPv4Range]] = Field(alias="remoteAddressRanges", default=None,)
	remotePortRanges: Optional[list[NumberRange]] = Field(alias="remotePortRanges", default=None,)
	routingPolicyType: Optional[VpnTrafficRuleRoutingPolicyType | str] = Field(alias="routingPolicyType", default=None,)
	vpnTrafficDirection: Optional[VpnTrafficDirection | str] = Field(alias="vpnTrafficDirection", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .vpn_traffic_rule_app_type import VpnTrafficRuleAppType
from .i_pv4_range import IPv4Range
from .number_range import NumberRange
from .i_pv4_range import IPv4Range
from .number_range import NumberRange
from .vpn_traffic_rule_routing_policy_type import VpnTrafficRuleRoutingPolicyType
from .vpn_traffic_direction import VpnTrafficDirection

