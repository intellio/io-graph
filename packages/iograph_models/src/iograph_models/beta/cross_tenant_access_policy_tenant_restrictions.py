from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyTenantRestrictions(BaseModel):
	applications: Optional[CrossTenantAccessPolicyTargetConfiguration] = Field(alias="applications", default=None,)
	usersAndGroups: Optional[CrossTenantAccessPolicyTargetConfiguration] = Field(alias="usersAndGroups", default=None,)
	odata_type: Literal["#microsoft.graph.crossTenantAccessPolicyTenantRestrictions"] = Field(alias="@odata.type", default="#microsoft.graph.crossTenantAccessPolicyTenantRestrictions")
	devices: Optional[DevicesFilter] = Field(alias="devices", default=None,)

from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
from .devices_filter import DevicesFilter
