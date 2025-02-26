from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicyAssignment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	policyId: Optional[str] = Field(default=None,alias="policyId",)
	roleDefinitionId: Optional[str] = Field(default=None,alias="roleDefinitionId",)
	scopeId: Optional[str] = Field(default=None,alias="scopeId",)
	scopeType: Optional[str] = Field(default=None,alias="scopeType",)
	policy: Optional[UnifiedRoleManagementPolicy] = Field(default=None,alias="policy",)

from .unified_role_management_policy import UnifiedRoleManagementPolicy

