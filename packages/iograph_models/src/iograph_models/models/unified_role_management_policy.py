from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isOrganizationDefault: Optional[bool] = Field(default=None,alias="isOrganizationDefault",)
	lastModifiedBy: Optional[Identity] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	scopeId: Optional[str] = Field(default=None,alias="scopeId",)
	scopeType: Optional[str] = Field(default=None,alias="scopeType",)
	effectiveRules: list[UnifiedRoleManagementPolicyRule] = Field(alias="effectiveRules",)
	rules: list[UnifiedRoleManagementPolicyRule] = Field(alias="rules",)

from .identity import Identity
from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

