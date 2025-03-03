from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyTargetConfiguration(BaseModel):
	accessType: Optional[CrossTenantAccessPolicyTargetConfigurationAccessType] = Field(default=None,alias="accessType",)
	targets: Optional[list[CrossTenantAccessPolicyTarget]] = Field(default=None,alias="targets",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cross_tenant_access_policy_target_configuration_access_type import CrossTenantAccessPolicyTargetConfigurationAccessType
from .cross_tenant_access_policy_target import CrossTenantAccessPolicyTarget

