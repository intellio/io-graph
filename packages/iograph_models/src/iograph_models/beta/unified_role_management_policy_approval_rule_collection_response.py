from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRoleManagementPolicyApprovalRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[UnifiedRoleManagementPolicyApprovalRule]] = Field(alias="value",default=None,)

from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule

