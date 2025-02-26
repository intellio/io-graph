from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CrossTenantAccessPolicy] = Field(alias="value",)

from .cross_tenant_access_policy import CrossTenantAccessPolicy

