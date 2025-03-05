from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyAuthenticationContextRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(default=None,alias="target",)
	claimValue: Optional[str] = Field(default=None,alias="claimValue",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

