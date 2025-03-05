from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyEnablementRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(default=None,alias="target",)
	enabledRules: Optional[list[str]] = Field(default=None,alias="enabledRules",)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

