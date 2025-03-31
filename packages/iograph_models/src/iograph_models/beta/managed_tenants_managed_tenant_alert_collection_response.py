from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsManagedTenantAlertCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedTenantsManagedTenantAlert]] = Field(alias="value", default=None,)

from .managed_tenants_managed_tenant_alert import ManagedTenantsManagedTenantAlert
