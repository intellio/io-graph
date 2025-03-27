from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementActionTenantDeploymentStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	statuses: Optional[list[ManagedTenantsManagementActionDeploymentStatus]] = Field(alias="statuses", default=None,)
	tenantGroupId: Optional[str] = Field(alias="tenantGroupId", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

from .managed_tenants_management_action_deployment_status import ManagedTenantsManagementActionDeploymentStatus

