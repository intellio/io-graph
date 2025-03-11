from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementActionTenantDeploymentStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ManagedTenantsManagementActionTenantDeploymentStatus]] = Field(alias="value",default=None,)

from .managed_tenants_management_action_tenant_deployment_status import ManagedTenantsManagementActionTenantDeploymentStatus

