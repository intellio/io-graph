from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PolicyRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activityBasedTimeoutPolicies: Optional[list[ActivityBasedTimeoutPolicy]] = Field(alias="activityBasedTimeoutPolicies", default=None,)
	adminConsentRequestPolicy: Optional[AdminConsentRequestPolicy] = Field(alias="adminConsentRequestPolicy", default=None,)
	appManagementPolicies: Optional[list[AppManagementPolicy]] = Field(alias="appManagementPolicies", default=None,)
	authenticationFlowsPolicy: Optional[AuthenticationFlowsPolicy] = Field(alias="authenticationFlowsPolicy", default=None,)
	authenticationMethodsPolicy: Optional[AuthenticationMethodsPolicy] = Field(alias="authenticationMethodsPolicy", default=None,)
	authenticationStrengthPolicies: Optional[list[AuthenticationStrengthPolicy]] = Field(alias="authenticationStrengthPolicies", default=None,)
	authorizationPolicy: Optional[AuthorizationPolicy] = Field(alias="authorizationPolicy", default=None,)
	claimsMappingPolicies: Optional[list[ClaimsMappingPolicy]] = Field(alias="claimsMappingPolicies", default=None,)
	conditionalAccessPolicies: Optional[list[ConditionalAccessPolicy]] = Field(alias="conditionalAccessPolicies", default=None,)
	crossTenantAccessPolicy: Optional[CrossTenantAccessPolicy] = Field(alias="crossTenantAccessPolicy", default=None,)
	defaultAppManagementPolicy: Optional[TenantAppManagementPolicy] = Field(alias="defaultAppManagementPolicy", default=None,)
	deviceRegistrationPolicy: Optional[DeviceRegistrationPolicy] = Field(alias="deviceRegistrationPolicy", default=None,)
	featureRolloutPolicies: Optional[list[FeatureRolloutPolicy]] = Field(alias="featureRolloutPolicies", default=None,)
	homeRealmDiscoveryPolicies: Optional[list[HomeRealmDiscoveryPolicy]] = Field(alias="homeRealmDiscoveryPolicies", default=None,)
	identitySecurityDefaultsEnforcementPolicy: Optional[IdentitySecurityDefaultsEnforcementPolicy] = Field(alias="identitySecurityDefaultsEnforcementPolicy", default=None,)
	permissionGrantPolicies: Optional[list[PermissionGrantPolicy]] = Field(alias="permissionGrantPolicies", default=None,)
	roleManagementPolicies: Optional[list[UnifiedRoleManagementPolicy]] = Field(alias="roleManagementPolicies", default=None,)
	roleManagementPolicyAssignments: Optional[list[UnifiedRoleManagementPolicyAssignment]] = Field(alias="roleManagementPolicyAssignments", default=None,)
	tokenIssuancePolicies: Optional[list[TokenIssuancePolicy]] = Field(alias="tokenIssuancePolicies", default=None,)
	tokenLifetimePolicies: Optional[list[TokenLifetimePolicy]] = Field(alias="tokenLifetimePolicies", default=None,)

from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .admin_consent_request_policy import AdminConsentRequestPolicy
from .app_management_policy import AppManagementPolicy
from .authentication_flows_policy import AuthenticationFlowsPolicy
from .authentication_methods_policy import AuthenticationMethodsPolicy
from .authentication_strength_policy import AuthenticationStrengthPolicy
from .authorization_policy import AuthorizationPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .conditional_access_policy import ConditionalAccessPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .device_registration_policy import DeviceRegistrationPolicy
from .feature_rollout_policy import FeatureRolloutPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .unified_role_management_policy import UnifiedRoleManagementPolicy
from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy

