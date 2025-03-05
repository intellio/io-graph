from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PolicyTemplate(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	multiTenantOrganizationIdentitySynchronization: Optional[MultiTenantOrganizationIdentitySyncPolicyTemplate] = Field(default=None,alias="multiTenantOrganizationIdentitySynchronization",)
	multiTenantOrganizationPartnerConfiguration: Optional[MultiTenantOrganizationPartnerConfigurationTemplate] = Field(default=None,alias="multiTenantOrganizationPartnerConfiguration",)

from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate

