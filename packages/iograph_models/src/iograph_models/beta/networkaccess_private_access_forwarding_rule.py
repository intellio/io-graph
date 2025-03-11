from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessPrivateAccessForwardingRule(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	action: Optional[NetworkaccessForwardingRuleAction | str] = Field(alias="action",default=None,)
	destinations: SerializeAsAny[Optional[list[NetworkaccessRuleDestination]]] = Field(alias="destinations",default=None,)
	ruleType: Optional[NetworkaccessNetworkDestinationType | str] = Field(alias="ruleType",default=None,)

from .networkaccess_forwarding_rule_action import NetworkaccessForwardingRuleAction
from .networkaccess_rule_destination import NetworkaccessRuleDestination
from .networkaccess_network_destination_type import NetworkaccessNetworkDestinationType

