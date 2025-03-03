from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MultiTenantOrganizationMemberCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MultiTenantOrganizationMember]] = Field(default=None,alias="value",)

from .multi_tenant_organization_member import MultiTenantOrganizationMember

