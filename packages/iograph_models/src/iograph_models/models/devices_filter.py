from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DevicesFilter(BaseModel):
	mode: Optional[CrossTenantAccessPolicyTargetConfigurationAccessType] = Field(default=None,alias="mode",)
	rule: Optional[str] = Field(default=None,alias="rule",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cross_tenant_access_policy_target_configuration_access_type import CrossTenantAccessPolicyTargetConfigurationAccessType

