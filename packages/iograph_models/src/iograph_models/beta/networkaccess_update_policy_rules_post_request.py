from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Networkaccess_update_policy_rulesPostRequest(BaseModel):
	rules: Optional[list[NetworkaccessPolicyRuleDelta]] = Field(alias="rules", default=None,)

from .networkaccess_policy_rule_delta import NetworkaccessPolicyRuleDelta

