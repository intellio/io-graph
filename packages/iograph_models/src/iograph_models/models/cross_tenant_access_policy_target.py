from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyTarget(BaseModel):
	target: Optional[str] = Field(default=None,alias="target",)
	targetType: Optional[CrossTenantAccessPolicyTargetType] = Field(default=None,alias="targetType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cross_tenant_access_policy_target_type import CrossTenantAccessPolicyTargetType

