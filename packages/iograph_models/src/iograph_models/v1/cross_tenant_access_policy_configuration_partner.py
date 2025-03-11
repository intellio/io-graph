from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossTenantAccessPolicyConfigurationPartner(BaseModel):
	automaticUserConsentSettings: Optional[InboundOutboundPolicyConfiguration] = Field(alias="automaticUserConsentSettings",default=None,)
	b2bCollaborationInbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bCollaborationInbound",default=None,)
	b2bCollaborationOutbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bCollaborationOutbound",default=None,)
	b2bDirectConnectInbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bDirectConnectInbound",default=None,)
	b2bDirectConnectOutbound: SerializeAsAny[Optional[CrossTenantAccessPolicyB2BSetting]] = Field(alias="b2bDirectConnectOutbound",default=None,)
	inboundTrust: Optional[CrossTenantAccessPolicyInboundTrust] = Field(alias="inboundTrust",default=None,)
	isInMultiTenantOrganization: Optional[bool] = Field(alias="isInMultiTenantOrganization",default=None,)
	isServiceProvider: Optional[bool] = Field(alias="isServiceProvider",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	tenantRestrictions: Optional[CrossTenantAccessPolicyTenantRestrictions] = Field(alias="tenantRestrictions",default=None,)
	identitySynchronization: Optional[CrossTenantIdentitySyncPolicyPartner] = Field(alias="identitySynchronization",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .inbound_outbound_policy_configuration import InboundOutboundPolicyConfiguration
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_b2_b_setting import CrossTenantAccessPolicyB2BSetting
from .cross_tenant_access_policy_inbound_trust import CrossTenantAccessPolicyInboundTrust
from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions
from .cross_tenant_identity_sync_policy_partner import CrossTenantIdentitySyncPolicyPartner

