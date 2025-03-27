from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyAuthenticationContextRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule")
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(alias="target", default=None,)
	claimValue: Optional[str] = Field(alias="claimValue", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

