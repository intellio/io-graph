from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsSetting(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	jsonValue: Optional[str] = Field(alias="jsonValue", default=None,)
	overwriteAllowed: Optional[bool] = Field(alias="overwriteAllowed", default=None,)
	settingId: Optional[str] = Field(alias="settingId", default=None,)
	valueType: Optional[ManagedTenantsManagementParameterValueType | str] = Field(alias="valueType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_management_parameter_value_type import ManagedTenantsManagementParameterValueType

