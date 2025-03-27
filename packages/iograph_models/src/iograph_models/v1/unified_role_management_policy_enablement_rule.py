from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyEnablementRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleManagementPolicyEnablementRule"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleManagementPolicyEnablementRule")
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(alias="target", default=None,)
	enabledRules: Optional[list[str]] = Field(alias="enabledRules", default=None,)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

