from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PolicyRoot(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activityBasedTimeoutPolicies: Optional[list[ActivityBasedTimeoutPolicy]] = Field(default=None,alias="activityBasedTimeoutPolicies",)
	adminConsentRequestPolicy: Optional[AdminConsentRequestPolicy] = Field(default=None,alias="adminConsentRequestPolicy",)
	appManagementPolicies: Optional[list[AppManagementPolicy]] = Field(default=None,alias="appManagementPolicies",)
	authenticationFlowsPolicy: Optional[AuthenticationFlowsPolicy] = Field(default=None,alias="authenticationFlowsPolicy",)
	authenticationMethodsPolicy: Optional[AuthenticationMethodsPolicy] = Field(default=None,alias="authenticationMethodsPolicy",)
	authenticationStrengthPolicies: Optional[list[AuthenticationStrengthPolicy]] = Field(default=None,alias="authenticationStrengthPolicies",)
	authorizationPolicy: Optional[AuthorizationPolicy] = Field(default=None,alias="authorizationPolicy",)
	claimsMappingPolicies: Optional[list[ClaimsMappingPolicy]] = Field(default=None,alias="claimsMappingPolicies",)
	conditionalAccessPolicies: Optional[list[ConditionalAccessPolicy]] = Field(default=None,alias="conditionalAccessPolicies",)
	crossTenantAccessPolicy: Optional[CrossTenantAccessPolicy] = Field(default=None,alias="crossTenantAccessPolicy",)
	defaultAppManagementPolicy: Optional[TenantAppManagementPolicy] = Field(default=None,alias="defaultAppManagementPolicy",)
	deviceRegistrationPolicy: Optional[DeviceRegistrationPolicy] = Field(default=None,alias="deviceRegistrationPolicy",)
	featureRolloutPolicies: Optional[list[FeatureRolloutPolicy]] = Field(default=None,alias="featureRolloutPolicies",)
	homeRealmDiscoveryPolicies: Optional[list[HomeRealmDiscoveryPolicy]] = Field(default=None,alias="homeRealmDiscoveryPolicies",)
	identitySecurityDefaultsEnforcementPolicy: Optional[IdentitySecurityDefaultsEnforcementPolicy] = Field(default=None,alias="identitySecurityDefaultsEnforcementPolicy",)
	permissionGrantPolicies: Optional[list[PermissionGrantPolicy]] = Field(default=None,alias="permissionGrantPolicies",)
	roleManagementPolicies: Optional[list[UnifiedRoleManagementPolicy]] = Field(default=None,alias="roleManagementPolicies",)
	roleManagementPolicyAssignments: Optional[list[UnifiedRoleManagementPolicyAssignment]] = Field(default=None,alias="roleManagementPolicyAssignments",)
	tokenIssuancePolicies: Optional[list[TokenIssuancePolicy]] = Field(default=None,alias="tokenIssuancePolicies",)
	tokenLifetimePolicies: Optional[list[TokenLifetimePolicy]] = Field(default=None,alias="tokenLifetimePolicies",)

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

