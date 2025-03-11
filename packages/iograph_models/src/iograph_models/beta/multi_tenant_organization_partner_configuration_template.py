from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganizationPartnerConfigurationTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	automaticUserConsentSettings: Optional[InboundOutboundPolicyConfiguration] = Field(alias="automaticUserConsentSettings",default=None,)
	b2bCollaborationInbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bCollaborationInbound",default=None,)
	b2bCollaborationOutbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bCollaborationOutbound",default=None,)
	b2bDirectConnectInbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bDirectConnectInbound",default=None,)
	b2bDirectConnectOutbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bDirectConnectOutbound",default=None,)
	inboundTrust: Optional[CrossTenantAccessPolicyInboundTrust] = Field(alias="inboundTrust",default=None,)
	templateApplicationLevel: Optional[TemplateApplicationLevel | str] = Field(alias="templateApplicationLevel",default=None,)

from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
from .template_application_level import TemplateApplicationLevel

