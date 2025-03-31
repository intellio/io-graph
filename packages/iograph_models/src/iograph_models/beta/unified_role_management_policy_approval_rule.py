from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicyApprovalRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleManagementPolicyApprovalRule"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleManagementPolicyApprovalRule")
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(alias="target", default=None,)
	setting: Optional[ApprovalSettings] = Field(alias="setting", default=None,)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget
from .approval_settings import ApprovalSettings
