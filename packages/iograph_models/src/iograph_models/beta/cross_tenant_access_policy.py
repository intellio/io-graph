from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantAccessPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	definition: Optional[list[str]] = Field(alias="definition",default=None,)
	allowedCloudEndpoints: Optional[list[str]] = Field(alias="allowedCloudEndpoints",default=None,)
	default: Optional[CrossTenantAccessPolicyConfigurationDefault] = Field(alias="default",default=None,)
	partners: Optional[list[CrossTenantAccessPolicyConfigurationPartner]] = Field(alias="partners",default=None,)
	templates: Optional[PolicyTemplate] = Field(alias="templates",default=None,)

from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
from .cross_tenant_access_policy_configuration_partner import CrossTenantAccessPolicyConfigurationPartner
from .policy_template import PolicyTemplate

