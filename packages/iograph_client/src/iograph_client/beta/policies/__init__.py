# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .token_lifetime_policies import TokenLifetimePoliciesRequest
	from .token_issuance_policies import TokenIssuancePoliciesRequest
	from .service_principal_creation_policies import ServicePrincipalCreationPoliciesRequest
	from .role_management_policy_assignments import RoleManagementPolicyAssignmentsRequest
	from .role_management_policies import RoleManagementPoliciesRequest
	from .permission_grant_pre_approval_policies import PermissionGrantPreApprovalPoliciesRequest
	from .permission_grant_policies import PermissionGrantPoliciesRequest
	from .mobile_device_management_policies import MobileDeviceManagementPoliciesRequest
	from .mobile_app_management_policies import MobileAppManagementPoliciesRequest
	from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicyRequest
	from .home_realm_discovery_policies import HomeRealmDiscoveryPoliciesRequest
	from .federated_token_validation_policy import FederatedTokenValidationPolicyRequest
	from .feature_rollout_policies import FeatureRolloutPoliciesRequest
	from .external_identities_policy import ExternalIdentitiesPolicyRequest
	from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicyRequest
	from .device_registration_policy import DeviceRegistrationPolicyRequest
	from .default_app_management_policy import DefaultAppManagementPolicyRequest
	from .cross_tenant_access_policy import CrossTenantAccessPolicyRequest
	from .conditional_access_policies import ConditionalAccessPoliciesRequest
	from .claims_mapping_policies import ClaimsMappingPoliciesRequest
	from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicyRequest
	from .authorization_policy import AuthorizationPolicyRequest
	from .authentication_strength_policies import AuthenticationStrengthPoliciesRequest
	from .authentication_methods_policy import AuthenticationMethodsPolicyRequest
	from .authentication_flows_policy import AuthenticationFlowsPolicyRequest
	from .app_management_policies import AppManagementPoliciesRequest
	from .admin_consent_request_policy import AdminConsentRequestPolicyRequest
	from .activity_based_timeout_policies import ActivityBasedTimeoutPoliciesRequest
	from .access_review_policy import AccessReviewPolicyRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.policy_root import PolicyRoot


class PoliciesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PolicyRoot:
		"""
		Get policies
		
		"""
		tags = ['policies.policyRoot']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.GET,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_async(request_info, PolicyRoot, error_mapping)

	async def patch(
		self,
		body: PolicyRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PolicyRoot:
		"""
		Update policies
		
		"""
		tags = ['policies.policyRoot']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, PolicyRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PoliciesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PoliciesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def access_review_policy(self,
	) -> AccessReviewPolicyRequest:
		from .access_review_policy import AccessReviewPolicyRequest
		return AccessReviewPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def activity_based_timeout_policies(self,
	) -> ActivityBasedTimeoutPoliciesRequest:
		from .activity_based_timeout_policies import ActivityBasedTimeoutPoliciesRequest
		return ActivityBasedTimeoutPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def admin_consent_request_policy(self,
	) -> AdminConsentRequestPolicyRequest:
		from .admin_consent_request_policy import AdminConsentRequestPolicyRequest
		return AdminConsentRequestPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def app_management_policies(self,
	) -> AppManagementPoliciesRequest:
		from .app_management_policies import AppManagementPoliciesRequest
		return AppManagementPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_flows_policy(self,
	) -> AuthenticationFlowsPolicyRequest:
		from .authentication_flows_policy import AuthenticationFlowsPolicyRequest
		return AuthenticationFlowsPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_methods_policy(self,
	) -> AuthenticationMethodsPolicyRequest:
		from .authentication_methods_policy import AuthenticationMethodsPolicyRequest
		return AuthenticationMethodsPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_strength_policies(self,
	) -> AuthenticationStrengthPoliciesRequest:
		from .authentication_strength_policies import AuthenticationStrengthPoliciesRequest
		return AuthenticationStrengthPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def authorization_policy(self,
	) -> AuthorizationPolicyRequest:
		from .authorization_policy import AuthorizationPolicyRequest
		return AuthorizationPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def b2c_authentication_methods_policy(self,
	) -> B2cAuthenticationMethodsPolicyRequest:
		from .b2c_authentication_methods_policy import B2cAuthenticationMethodsPolicyRequest
		return B2cAuthenticationMethodsPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def claims_mapping_policies(self,
	) -> ClaimsMappingPoliciesRequest:
		from .claims_mapping_policies import ClaimsMappingPoliciesRequest
		return ClaimsMappingPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def conditional_access_policies(self,
	) -> ConditionalAccessPoliciesRequest:
		from .conditional_access_policies import ConditionalAccessPoliciesRequest
		return ConditionalAccessPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def cross_tenant_access_policy(self,
	) -> CrossTenantAccessPolicyRequest:
		from .cross_tenant_access_policy import CrossTenantAccessPolicyRequest
		return CrossTenantAccessPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def default_app_management_policy(self,
	) -> DefaultAppManagementPolicyRequest:
		from .default_app_management_policy import DefaultAppManagementPolicyRequest
		return DefaultAppManagementPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def device_registration_policy(self,
	) -> DeviceRegistrationPolicyRequest:
		from .device_registration_policy import DeviceRegistrationPolicyRequest
		return DeviceRegistrationPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def directory_role_access_review_policy(self,
	) -> DirectoryRoleAccessReviewPolicyRequest:
		from .directory_role_access_review_policy import DirectoryRoleAccessReviewPolicyRequest
		return DirectoryRoleAccessReviewPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def external_identities_policy(self,
	) -> ExternalIdentitiesPolicyRequest:
		from .external_identities_policy import ExternalIdentitiesPolicyRequest
		return ExternalIdentitiesPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def feature_rollout_policies(self,
	) -> FeatureRolloutPoliciesRequest:
		from .feature_rollout_policies import FeatureRolloutPoliciesRequest
		return FeatureRolloutPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def federated_token_validation_policy(self,
	) -> FederatedTokenValidationPolicyRequest:
		from .federated_token_validation_policy import FederatedTokenValidationPolicyRequest
		return FederatedTokenValidationPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def home_realm_discovery_policies(self,
	) -> HomeRealmDiscoveryPoliciesRequest:
		from .home_realm_discovery_policies import HomeRealmDiscoveryPoliciesRequest
		return HomeRealmDiscoveryPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_security_defaults_enforcement_policy(self,
	) -> IdentitySecurityDefaultsEnforcementPolicyRequest:
		from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicyRequest
		return IdentitySecurityDefaultsEnforcementPolicyRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_app_management_policies(self,
	) -> MobileAppManagementPoliciesRequest:
		from .mobile_app_management_policies import MobileAppManagementPoliciesRequest
		return MobileAppManagementPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_device_management_policies(self,
	) -> MobileDeviceManagementPoliciesRequest:
		from .mobile_device_management_policies import MobileDeviceManagementPoliciesRequest
		return MobileDeviceManagementPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def permission_grant_policies(self,
	) -> PermissionGrantPoliciesRequest:
		from .permission_grant_policies import PermissionGrantPoliciesRequest
		return PermissionGrantPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def permission_grant_pre_approval_policies(self,
	) -> PermissionGrantPreApprovalPoliciesRequest:
		from .permission_grant_pre_approval_policies import PermissionGrantPreApprovalPoliciesRequest
		return PermissionGrantPreApprovalPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_management_policies(self,
	) -> RoleManagementPoliciesRequest:
		from .role_management_policies import RoleManagementPoliciesRequest
		return RoleManagementPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def role_management_policy_assignments(self,
	) -> RoleManagementPolicyAssignmentsRequest:
		from .role_management_policy_assignments import RoleManagementPolicyAssignmentsRequest
		return RoleManagementPolicyAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def service_principal_creation_policies(self,
	) -> ServicePrincipalCreationPoliciesRequest:
		from .service_principal_creation_policies import ServicePrincipalCreationPoliciesRequest
		return ServicePrincipalCreationPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def token_issuance_policies(self,
	) -> TokenIssuancePoliciesRequest:
		from .token_issuance_policies import TokenIssuancePoliciesRequest
		return TokenIssuancePoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def token_lifetime_policies(self,
	) -> TokenLifetimePoliciesRequest:
		from .token_lifetime_policies import TokenLifetimePoliciesRequest
		return TokenLifetimePoliciesRequest(self.request_adapter, self.path_parameters)

