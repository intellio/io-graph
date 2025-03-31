from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagementTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managementTemplate"] = Field(alias="@odata.type",)
	category: Optional[ManagedTenantsManagementCategory | str] = Field(alias="category", default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationLinks: Optional[list[ActionUrl]] = Field(alias="informationLinks", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	parameters: Optional[list[ManagedTenantsTemplateParameter]] = Field(alias="parameters", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	provider: Optional[ManagedTenantsManagementProvider | str] = Field(alias="provider", default=None,)
	userImpact: Optional[str] = Field(alias="userImpact", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	workloadActions: Optional[list[ManagedTenantsWorkloadAction]] = Field(alias="workloadActions", default=None,)
	managementTemplateCollections: Optional[list[ManagedTenantsManagementTemplateCollection]] = Field(alias="managementTemplateCollections", default=None,)
	managementTemplateSteps: Optional[list[ManagedTenantsManagementTemplateStep]] = Field(alias="managementTemplateSteps", default=None,)

from .managed_tenants_management_category import ManagedTenantsManagementCategory
from .action_url import ActionUrl
from .managed_tenants_template_parameter import ManagedTenantsTemplateParameter
from .managed_tenants_management_provider import ManagedTenantsManagementProvider
from .managed_tenants_workload_action import ManagedTenantsWorkloadAction
from .managed_tenants_management_template_collection import ManagedTenantsManagementTemplateCollection
from .managed_tenants_management_template_step import ManagedTenantsManagementTemplateStep
