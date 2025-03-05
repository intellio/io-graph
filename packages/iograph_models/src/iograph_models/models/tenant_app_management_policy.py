from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TenantAppManagementPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	applicationRestrictions: Optional[AppManagementApplicationConfiguration] = Field(default=None,alias="applicationRestrictions",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	servicePrincipalRestrictions: Optional[AppManagementServicePrincipalConfiguration] = Field(default=None,alias="servicePrincipalRestrictions",)

from .app_management_application_configuration import AppManagementApplicationConfiguration
from .app_management_service_principal_configuration import AppManagementServicePrincipalConfiguration

