from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicyApprovalRule(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(default=None,alias="target",)
	setting: Optional[ApprovalSettings] = Field(default=None,alias="setting",)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget
from .approval_settings import ApprovalSettings

