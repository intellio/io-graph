from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessPolicyRuleDelta(BaseModel):
	action: Optional[NetworkaccessForwardingRuleAction | str] = Field(alias="action", default=None,)
	ruleId: Optional[str] = Field(alias="ruleId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_forwarding_rule_action import NetworkaccessForwardingRuleAction
