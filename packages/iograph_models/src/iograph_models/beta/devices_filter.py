from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DevicesFilter(BaseModel):
	mode: Optional[CrossTenantAccessPolicyTargetConfigurationAccessType | str] = Field(alias="mode", default=None,)
	rule: Optional[str] = Field(alias="rule", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cross_tenant_access_policy_target_configuration_access_type import CrossTenantAccessPolicyTargetConfigurationAccessType
