from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class TenantAppManagementPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.tenantAppManagementPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.tenantAppManagementPolicy")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	applicationRestrictions: Optional[AppManagementApplicationConfiguration] = Field(alias="applicationRestrictions", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	servicePrincipalRestrictions: Optional[AppManagementServicePrincipalConfiguration] = Field(alias="servicePrincipalRestrictions", default=None,)

from .app_management_application_configuration import AppManagementApplicationConfiguration
from .app_management_service_principal_configuration import AppManagementServicePrincipalConfiguration
