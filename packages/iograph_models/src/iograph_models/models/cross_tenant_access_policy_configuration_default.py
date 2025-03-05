from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantAccessPolicyConfigurationDefault(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	automaticUserConsentSettings: Optional[InboundOutboundPolicyConfiguration] = Field(default=None,alias="automaticUserConsentSettings",)
	b2bCollaborationInbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(default=None,alias="b2bCollaborationInbound",)
	b2bCollaborationOutbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(default=None,alias="b2bCollaborationOutbound",)
	b2bDirectConnectInbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(default=None,alias="b2bDirectConnectInbound",)
	b2bDirectConnectOutbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(default=None,alias="b2bDirectConnectOutbound",)
	inboundTrust: Optional[CrossTenantAccessPolicyInboundTrust] = Field(default=None,alias="inboundTrust",)
	invitationRedemptionIdentityProviderConfiguration: Optional[DefaultInvitationRedemptionIdentityProviderConfiguration] = Field(default=None,alias="invitationRedemptionIdentityProviderConfiguration",)
	isServiceDefault: Optional[bool] = Field(default=None,alias="isServiceDefault",)
	tenantRestrictions: Optional[CrossTenantAccessPolicyTenantRestrictions] = Field(default=None,alias="tenantRestrictions",)

from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
from .default_invitation_redemption_identity_provider_configuration import DefaultInvitationRedemptionIdentityProviderConfiguration
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions

