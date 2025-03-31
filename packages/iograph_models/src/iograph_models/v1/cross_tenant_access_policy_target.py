from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyTarget(BaseModel):
	target: Optional[str] = Field(alias="target", default=None,)
	targetType: Optional[CrossTenantAccessPolicyTargetType | str] = Field(alias="targetType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cross_tenant_access_policy_target_type import CrossTenantAccessPolicyTargetType
