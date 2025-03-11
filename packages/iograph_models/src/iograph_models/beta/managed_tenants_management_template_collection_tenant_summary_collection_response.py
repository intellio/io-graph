from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementTemplateCollectionTenantSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ManagedTenantsManagementTemplateCollectionTenantSummary]] = Field(alias="value",default=None,)

from .managed_tenants_management_template_collection_tenant_summary import ManagedTenantsManagementTemplateCollectionTenantSummary

