from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagementTemplateStepVersion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managementTemplateStepVersion"] = Field(alias="@odata.type",)
	contentMarkdown: Optional[str] = Field(alias="contentMarkdown", default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	versionInformation: Optional[str] = Field(alias="versionInformation", default=None,)
	acceptedFor: Optional[ManagedTenantsManagementTemplateStep] = Field(alias="acceptedFor", default=None,)
	deployments: Optional[list[ManagedTenantsManagementTemplateStepDeployment]] = Field(alias="deployments", default=None,)
	templateStep: Optional[ManagedTenantsManagementTemplateStep] = Field(alias="templateStep", default=None,)

from .managed_tenants_management_template_step import ManagedTenantsManagementTemplateStep
from .managed_tenants_management_template_step_deployment import ManagedTenantsManagementTemplateStepDeployment
