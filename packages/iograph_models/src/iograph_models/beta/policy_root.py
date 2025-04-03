from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class PolicyRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.policyRoot"] = Field(alias="@odata.type", default="#microsoft.graph.policyRoot")
	accessReviewPolicy: Optional[AccessReviewPolicy] = Field(alias="accessReviewPolicy", default=None,)
	activityBasedTimeoutPolicies: Optional[list[ActivityBasedTimeoutPolicy]] = Field(alias="activityBasedTimeoutPolicies", default=None,)
	adminConsentRequestPolicy: Optional[AdminConsentRequestPolicy] = Field(alias="adminConsentRequestPolicy", default=None,)
	appManagementPolicies: Optional[list[AppManagementPolicy]] = Field(alias="appManagementPolicies", default=None,)
	authenticationFlowsPolicy: Optional[AuthenticationFlowsPolicy] = Field(alias="authenticationFlowsPolicy", default=None,)
	authenticationMethodsPolicy: Optional[AuthenticationMethodsPolicy] = Field(alias="authenticationMethodsPolicy", default=None,)
	authenticationStrengthPolicies: Optional[list[AuthenticationStrengthPolicy]] = Field(alias="authenticationStrengthPolicies", default=None,)
	authorizationPolicy: Optional[list[AuthorizationPolicy]] = Field(alias="authorizationPolicy", default=None,)
	b2cAuthenticationMethodsPolicy: Optional[B2cAuthenticationMethodsPolicy] = Field(alias="b2cAuthenticationMethodsPolicy", default=None,)
	claimsMappingPolicies: Optional[list[ClaimsMappingPolicy]] = Field(alias="claimsMappingPolicies", default=None,)
	conditionalAccessPolicies: Optional[list[Annotated[Union[ConditionalAccessWhatIfPolicy],Field(discriminator="odata_type")]]] = Field(alias="conditionalAccessPolicies", default=None,)
	crossTenantAccessPolicy: Optional[CrossTenantAccessPolicy] = Field(alias="crossTenantAccessPolicy", default=None,)
	defaultAppManagementPolicy: Optional[TenantAppManagementPolicy] = Field(alias="defaultAppManagementPolicy", default=None,)
	deviceRegistrationPolicy: Optional[DeviceRegistrationPolicy] = Field(alias="deviceRegistrationPolicy", default=None,)
	directoryRoleAccessReviewPolicy: Optional[DirectoryRoleAccessReviewPolicy] = Field(alias="directoryRoleAccessReviewPolicy", default=None,)
	externalIdentitiesPolicy: Optional[ExternalIdentitiesPolicy] = Field(alias="externalIdentitiesPolicy", default=None,)
	featureRolloutPolicies: Optional[list[FeatureRolloutPolicy]] = Field(alias="featureRolloutPolicies", default=None,)
	federatedTokenValidationPolicy: Optional[FederatedTokenValidationPolicy] = Field(alias="federatedTokenValidationPolicy", default=None,)
	homeRealmDiscoveryPolicies: Optional[list[HomeRealmDiscoveryPolicy]] = Field(alias="homeRealmDiscoveryPolicies", default=None,)
	identitySecurityDefaultsEnforcementPolicy: Optional[IdentitySecurityDefaultsEnforcementPolicy] = Field(alias="identitySecurityDefaultsEnforcementPolicy", default=None,)
	mobileAppManagementPolicies: Optional[list[MobilityManagementPolicy]] = Field(alias="mobileAppManagementPolicies", default=None,)
	mobileDeviceManagementPolicies: Optional[list[MobilityManagementPolicy]] = Field(alias="mobileDeviceManagementPolicies", default=None,)
	permissionGrantPolicies: Optional[list[PermissionGrantPolicy]] = Field(alias="permissionGrantPolicies", default=None,)
	permissionGrantPreApprovalPolicies: Optional[list[PermissionGrantPreApprovalPolicy]] = Field(alias="permissionGrantPreApprovalPolicies", default=None,)
	roleManagementPolicies: Optional[list[UnifiedRoleManagementPolicy]] = Field(alias="roleManagementPolicies", default=None,)
	roleManagementPolicyAssignments: Optional[list[UnifiedRoleManagementPolicyAssignment]] = Field(alias="roleManagementPolicyAssignments", default=None,)
	servicePrincipalCreationPolicies: Optional[list[ServicePrincipalCreationPolicy]] = Field(alias="servicePrincipalCreationPolicies", default=None,)
	tokenIssuancePolicies: Optional[list[TokenIssuancePolicy]] = Field(alias="tokenIssuancePolicies", default=None,)
	tokenLifetimePolicies: Optional[list[TokenLifetimePolicy]] = Field(alias="tokenLifetimePolicies", default=None,)

from .access_review_policy import AccessReviewPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .admin_consent_request_policy import AdminConsentRequestPolicy
from .app_management_policy import AppManagementPolicy
from .authentication_flows_policy import AuthenticationFlowsPolicy
from .authentication_methods_policy import AuthenticationMethodsPolicy
from .authentication_strength_policy import AuthenticationStrengthPolicy
from .authorization_policy import AuthorizationPolicy
from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .device_registration_policy import DeviceRegistrationPolicy
from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicy
from .external_identities_policy import ExternalIdentitiesPolicy
from .feature_rollout_policy import FeatureRolloutPolicy
from .federated_token_validation_policy import FederatedTokenValidationPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .mobility_management_policy import MobilityManagementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .permission_grant_pre_approval_policy import PermissionGrantPreApprovalPolicy
from .unified_role_management_policy import UnifiedRoleManagementPolicy
from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
from .service_principal_creation_policy import ServicePrincipalCreationPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
