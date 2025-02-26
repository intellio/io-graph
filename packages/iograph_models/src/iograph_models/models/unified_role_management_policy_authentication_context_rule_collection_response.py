from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UnifiedRoleManagementPolicyAuthenticationContextRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[UnifiedRoleManagementPolicyAuthenticationContextRule] = Field(alias="value",)

from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule

