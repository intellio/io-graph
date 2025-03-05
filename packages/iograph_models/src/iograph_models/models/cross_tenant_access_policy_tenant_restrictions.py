from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantAccessPolicyTenantRestrictions(BaseModel):
	applications: Optional[CrossTenantAccessPolicyTargetConfiguration] = Field(default=None,alias="applications",)
	usersAndGroups: Optional[CrossTenantAccessPolicyTargetConfiguration] = Field(default=None,alias="usersAndGroups",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	devices: Optional[DevicesFilter] = Field(default=None,alias="devices",)

from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
from .devices_filter import DevicesFilter

