from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PolicyRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activityBasedTimeoutPolicies: list[ActivityBasedTimeoutPolicy] = Field(alias="activityBasedTimeoutPolicies",)
	adminConsentRequestPolicy: Optional[AdminConsentRequestPolicy] = Field(default=None,alias="adminConsentRequestPolicy",)
	appManagementPolicies: list[AppManagementPolicy] = Field(alias="appManagementPolicies",)
	authenticationFlowsPolicy: Optional[AuthenticationFlowsPolicy] = Field(default=None,alias="authenticationFlowsPolicy",)
	authenticationMethodsPolicy: Optional[AuthenticationMethodsPolicy] = Field(default=None,alias="authenticationMethodsPolicy",)
	authenticationStrengthPolicies: list[AuthenticationStrengthPolicy] = Field(alias="authenticationStrengthPolicies",)
	authorizationPolicy: Optional[AuthorizationPolicy] = Field(default=None,alias="authorizationPolicy",)
	claimsMappingPolicies: list[ClaimsMappingPolicy] = Field(alias="claimsMappingPolicies",)
	conditionalAccessPolicies: list[ConditionalAccessPolicy] = Field(alias="conditionalAccessPolicies",)
	crossTenantAccessPolicy: Optional[CrossTenantAccessPolicy] = Field(default=None,alias="crossTenantAccessPolicy",)
	defaultAppManagementPolicy: Optional[TenantAppManagementPolicy] = Field(default=None,alias="defaultAppManagementPolicy",)
	deviceRegistrationPolicy: Optional[DeviceRegistrationPolicy] = Field(default=None,alias="deviceRegistrationPolicy",)
	featureRolloutPolicies: list[FeatureRolloutPolicy] = Field(alias="featureRolloutPolicies",)
	homeRealmDiscoveryPolicies: list[HomeRealmDiscoveryPolicy] = Field(alias="homeRealmDiscoveryPolicies",)
	identitySecurityDefaultsEnforcementPolicy: Optional[IdentitySecurityDefaultsEnforcementPolicy] = Field(default=None,alias="identitySecurityDefaultsEnforcementPolicy",)
	permissionGrantPolicies: list[PermissionGrantPolicy] = Field(alias="permissionGrantPolicies",)
	roleManagementPolicies: list[UnifiedRoleManagementPolicy] = Field(alias="roleManagementPolicies",)
	roleManagementPolicyAssignments: list[UnifiedRoleManagementPolicyAssignment] = Field(alias="roleManagementPolicyAssignments",)
	tokenIssuancePolicies: list[TokenIssuancePolicy] = Field(alias="tokenIssuancePolicies",)
	tokenLifetimePolicies: list[TokenLifetimePolicy] = Field(alias="tokenLifetimePolicies",)

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

