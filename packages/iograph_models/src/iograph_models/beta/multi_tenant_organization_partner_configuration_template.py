from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganizationPartnerConfigurationTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	automaticUserConsentSettings: Optional[InboundOutboundPolicyConfiguration] = Field(alias="automaticUserConsentSettings", default=None,)
	b2bCollaborationInbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bCollaborationInbound", default=None,discriminator="odata_type", )
	b2bCollaborationOutbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bCollaborationOutbound", default=None,discriminator="odata_type", )
	b2bDirectConnectInbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bDirectConnectInbound", default=None,discriminator="odata_type", )
	b2bDirectConnectOutbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bDirectConnectOutbound", default=None,discriminator="odata_type", )
	inboundTrust: Optional[CrossTenantAccessPolicyInboundTrust] = Field(alias="inboundTrust", default=None,)
	templateApplicationLevel: Optional[TemplateApplicationLevel | str] = Field(alias="templateApplicationLevel", default=None,)

from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
from .template_application_level import TemplateApplicationLevel

