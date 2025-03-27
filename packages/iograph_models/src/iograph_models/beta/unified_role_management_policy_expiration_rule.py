from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyExpirationRule(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"] = Field(alias="@odata.type", default="#microsoft.graph.unifiedRoleManagementPolicyExpirationRule")
	target: Optional[UnifiedRoleManagementPolicyRuleTarget] = Field(alias="target", default=None,)
	isExpirationRequired: Optional[bool] = Field(alias="isExpirationRequired", default=None,)
	maximumDuration: Optional[str] = Field(alias="maximumDuration", default=None,)

from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

