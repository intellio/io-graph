from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PolicyTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	multiTenantOrganizationIdentitySynchronization: Optional[MultiTenantOrganizationIdentitySyncPolicyTemplate] = Field(alias="multiTenantOrganizationIdentitySynchronization",default=None,)
	multiTenantOrganizationPartnerConfiguration: Optional[MultiTenantOrganizationPartnerConfigurationTemplate] = Field(alias="multiTenantOrganizationPartnerConfiguration",default=None,)

from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate

