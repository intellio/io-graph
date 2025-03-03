from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CrossTenantAccessPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	allowedCloudEndpoints: Optional[list[str]] = Field(default=None,alias="allowedCloudEndpoints",)
	default: Optional[CrossTenantAccessPolicyConfigurationDefault] = Field(default=None,alias="default",)
	partners: Optional[list[CrossTenantAccessPolicyConfigurationPartner]] = Field(default=None,alias="partners",)
	templates: Optional[PolicyTemplate] = Field(default=None,alias="templates",)

from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
from .policy_template import PolicyTemplate

