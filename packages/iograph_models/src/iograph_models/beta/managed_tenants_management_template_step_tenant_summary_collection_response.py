from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementTemplateStepTenantSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ManagedTenantsManagementTemplateStepTenantSummary]] = Field(alias="value",default=None,)

from .managed_tenants_management_template_step_tenant_summary import ManagedTenantsManagementTemplateStepTenantSummary

