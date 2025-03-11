from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isOrganizationDefault: Optional[bool] = Field(alias="isOrganizationDefault",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[Identity]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	scopeId: Optional[str] = Field(alias="scopeId",default=None,)
	scopeType: Optional[str] = Field(alias="scopeType",default=None,)
	effectiveRules: SerializeAsAny[Optional[list[UnifiedRoleManagementPolicyRule]]] = Field(alias="effectiveRules",default=None,)
	rules: SerializeAsAny[Optional[list[UnifiedRoleManagementPolicyRule]]] = Field(alias="rules",default=None,)

from .identity import Identity
from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

