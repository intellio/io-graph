from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[CrossTenantAccessPolicyTarget]] = Field(default=None,alias="value",)

from .cross_tenant_access_policy_target import CrossTenantAccessPolicyTarget

