from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsTemplateAction(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	service: Optional[str] = Field(alias="service",default=None,)
	settings: Optional[list[ManagedTenantsSetting]] = Field(alias="settings",default=None,)
	templateActionId: Optional[str] = Field(alias="templateActionId",default=None,)
	licenses: Optional[LicenseDetails] = Field(alias="licenses",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .managed_tenants_setting import ManagedTenantsSetting
from .license_details import LicenseDetails

