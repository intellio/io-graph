from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantAccessPolicyTenantRestrictions(BaseModel):
	applications: Optional[CrossTenantAccessPolicyTargetConfiguration] = Field(alias="applications",default=None,)
	usersAndGroups: Optional[CrossTenantAccessPolicyTargetConfiguration] = Field(alias="usersAndGroups",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	devices: Optional[DevicesFilter] = Field(alias="devices",default=None,)

from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
from .devices_filter import DevicesFilter

