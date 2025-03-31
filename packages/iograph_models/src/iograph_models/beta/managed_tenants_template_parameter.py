from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedTenantsTemplateParameter(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	jsonAllowedValues: Optional[str] = Field(alias="jsonAllowedValues", default=None,)
	jsonDefaultValue: Optional[str] = Field(alias="jsonDefaultValue", default=None,)
	valueType: Optional[ManagedTenantsManagementParameterValueType | str] = Field(alias="valueType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_tenants_management_parameter_value_type import ManagedTenantsManagementParameterValueType
