from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsManagementActionDeploymentStatus(BaseModel):
	managementActionId: Optional[str] = Field(alias="managementActionId", default=None,)
	managementTemplateId: Optional[str] = Field(alias="managementTemplateId", default=None,)
	managementTemplateVersion: Optional[int] = Field(alias="managementTemplateVersion", default=None,)
	status: Optional[ManagedTenantsManagementActionStatus | str] = Field(alias="status", default=None,)
	workloadActionDeploymentStatuses: Optional[list[ManagedTenantsWorkloadActionDeploymentStatus]] = Field(alias="workloadActionDeploymentStatuses", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_management_action_status import ManagedTenantsManagementActionStatus
from .managed_tenants_workload_action_deployment_status import ManagedTenantsWorkloadActionDeploymentStatus

