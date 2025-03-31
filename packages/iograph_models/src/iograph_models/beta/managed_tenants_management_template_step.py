from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagementTemplateStep(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managementTemplateStep"] = Field(alias="@odata.type",)
	category: Optional[ManagedTenantsManagementCategory | str] = Field(alias="category", default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	informationLinks: Optional[list[ActionUrl]] = Field(alias="informationLinks", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	portalLink: Optional[ActionUrl] = Field(alias="portalLink", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	userImpact: Optional[str] = Field(alias="userImpact", default=None,)
	acceptedVersion: Optional[ManagedTenantsManagementTemplateStepVersion] = Field(alias="acceptedVersion", default=None,)
	managementTemplate: Optional[ManagedTenantsManagementTemplate] = Field(alias="managementTemplate", default=None,)
	versions: Optional[list[ManagedTenantsManagementTemplateStepVersion]] = Field(alias="versions", default=None,)

from .managed_tenants_management_category import ManagedTenantsManagementCategory
from .action_url import ActionUrl
from .managed_tenants_management_template_step_version import ManagedTenantsManagementTemplateStepVersion
from .managed_tenants_management_template import ManagedTenantsManagementTemplate
