from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicyAssignment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRoleManagementPolicyAssignment"] = Field(alias="@odata.type",)
	policyId: Optional[str] = Field(alias="policyId", default=None,)
	roleDefinitionId: Optional[str] = Field(alias="roleDefinitionId", default=None,)
	scopeId: Optional[str] = Field(alias="scopeId", default=None,)
	scopeType: Optional[str] = Field(alias="scopeType", default=None,)
	policy: Optional[UnifiedRoleManagementPolicy] = Field(alias="policy", default=None,)

from .unified_role_management_policy import UnifiedRoleManagementPolicy
