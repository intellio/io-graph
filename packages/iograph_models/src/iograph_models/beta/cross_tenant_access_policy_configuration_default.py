from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyConfigurationDefault(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.crossTenantAccessPolicyConfigurationDefault"] = Field(alias="@odata.type", default="#microsoft.graph.crossTenantAccessPolicyConfigurationDefault")
	automaticUserConsentSettings: Optional[InboundOutboundPolicyConfiguration] = Field(alias="automaticUserConsentSettings", default=None,)
	b2bCollaborationInbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bCollaborationInbound", default=None,discriminator="odata_type", )
	b2bCollaborationOutbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bCollaborationOutbound", default=None,discriminator="odata_type", )
	b2bDirectConnectInbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bDirectConnectInbound", default=None,discriminator="odata_type", )
	b2bDirectConnectOutbound: Optional[Union[CrossTenantAccessPolicyTenantRestrictions]] = Field(alias="b2bDirectConnectOutbound", default=None,discriminator="odata_type", )
	inboundTrust: Optional[CrossTenantAccessPolicyInboundTrust] = Field(alias="inboundTrust", default=None,)
	invitationRedemptionIdentityProviderConfiguration: Optional[DefaultInvitationRedemptionIdentityProviderConfiguration] = Field(alias="invitationRedemptionIdentityProviderConfiguration", default=None,)
	isServiceDefault: Optional[bool] = Field(alias="isServiceDefault", default=None,)
	tenantRestrictions: Optional[CrossTenantAccessPolicyTenantRestrictions] = Field(alias="tenantRestrictions", default=None,)

from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration
