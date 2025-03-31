from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyTargetConfiguration(BaseModel):
	accessType: Optional[CrossTenantAccessPolicyTargetConfigurationAccessType | str] = Field(alias="accessType", default=None,)
	targets: Optional[list[CrossTenantAccessPolicyTarget]] = Field(alias="targets", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cross_tenant_access_policy_target_configuration_access_type import CrossTenantAccessPolicyTargetConfigurationAccessType
from .cross_tenant_access_policy_target import CrossTenantAccessPolicyTarget
