from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagementTemplateStepDeployment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managementTemplateStepDeployment"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.managementTemplateStepDeployment")
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	error: Optional[ManagedTenantsGraphAPIErrorDetails] = Field(alias="error", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	status: Optional[ManagedTenantsManagementTemplateDeploymentStatus | str] = Field(alias="status", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	templateStepVersion: Optional[ManagedTenantsManagementTemplateStepVersion] = Field(alias="templateStepVersion", default=None,)

from .managed_tenants_graph_a_p_i_error_details import ManagedTenantsGraphAPIErrorDetails
from .managed_tenants_management_template_deployment_status import ManagedTenantsManagementTemplateDeploymentStatus
from .managed_tenants_management_template_step_version import ManagedTenantsManagementTemplateStepVersion
