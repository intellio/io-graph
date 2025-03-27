from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VpnOnDemandRule(BaseModel):
	action: Optional[VpnOnDemandRuleConnectionAction | str] = Field(alias="action", default=None,)
	dnsSearchDomains: Optional[list[str]] = Field(alias="dnsSearchDomains", default=None,)
	dnsServerAddressMatch: Optional[list[str]] = Field(alias="dnsServerAddressMatch", default=None,)
	domainAction: Optional[VpnOnDemandRuleConnectionDomainAction | str] = Field(alias="domainAction", default=None,)
	domains: Optional[list[str]] = Field(alias="domains", default=None,)
	interfaceTypeMatch: Optional[VpnOnDemandRuleInterfaceTypeMatch | str] = Field(alias="interfaceTypeMatch", default=None,)
	probeRequiredUrl: Optional[str] = Field(alias="probeRequiredUrl", default=None,)
	probeUrl: Optional[str] = Field(alias="probeUrl", default=None,)
	ssids: Optional[list[str]] = Field(alias="ssids", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .vpn_on_demand_rule_connection_action import VpnOnDemandRuleConnectionAction
from .vpn_on_demand_rule_connection_domain_action import VpnOnDemandRuleConnectionDomainAction
from .vpn_on_demand_rule_interface_type_match import VpnOnDemandRuleInterfaceTypeMatch

