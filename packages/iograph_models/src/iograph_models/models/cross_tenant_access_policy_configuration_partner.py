from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyConfigurationPartner(BaseModel):
	automaticUserConsentSettings: Optional[InboundOutboundPolicyConfiguration] = Field(default=None,alias="automaticUserConsentSettings",)
	b2bCollaborationInbound: Optional[CrossTenantAccessPolicyB2BSetting] = Field(default=None,alias="b2bCollaborationInbound",)
	b2bCollaborationOutbound: Optional[CrossTenantAccessPolicyB2BSetting] = Field(default=None,alias="b2bCollaborationOutbound",)
	b2bDirectConnectInbound: Optional[CrossTenantAccessPolicyB2BSetting] = Field(default=None,alias="b2bDirectConnectInbound",)
	b2bDirectConnectOutbound: Optional[CrossTenantAccessPolicyB2BSetting] = Field(default=None,alias="b2bDirectConnectOutbound",)
	inboundTrust: Optional[CrossTenantAccessPolicyInboundTrust] = Field(default=None,alias="inboundTrust",)
	isInMultiTenantOrganization: Optional[bool] = Field(default=None,alias="isInMultiTenantOrganization",)
	isServiceProvider: Optional[bool] = Field(default=None,alias="isServiceProvider",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	tenantRestrictions: Optional[CrossTenantAccessPolicyTenantRestrictions] = Field(default=None,alias="tenantRestrictions",)
	identitySynchronization: Optional[CrossTenantIdentitySyncPolicyPartner] = Field(default=None,alias="identitySynchronization",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner

