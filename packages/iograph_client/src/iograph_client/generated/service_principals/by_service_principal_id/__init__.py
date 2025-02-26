# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .transitive_member_of import TransitiveMemberOfRequest
	from .token_lifetime_policies import TokenLifetimePoliciesRequest
	from .token_issuance_policies import TokenIssuancePoliciesRequest
	from .synchronization import SynchronizationRequest
	from .remote_desktop_security_configuration import RemoteDesktopSecurityConfigurationRequest
	from .owners import OwnersRequest
	from .owned_objects import OwnedObjectsRequest
	from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
	from .restore import RestoreRequest
	from .remove_password import RemovePasswordRequest
	from .remove_key import RemoveKeyRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .add_token_signing_certificate import AddTokenSigningCertificateRequest
	from .add_password import AddPasswordRequest
	from .add_key import AddKeyRequest
	from .member_of import MemberOfRequest
	from .home_realm_discovery_policies import HomeRealmDiscoveryPoliciesRequest
	from .federated_identity_credentials import FederatedIdentityCredentialsRequest
	from .endpoints import EndpointsRequest
	from .delegated_permission_classifications import DelegatedPermissionClassificationsRequest
	from .created_objects import CreatedObjectsRequest
	from .claims_mapping_policies import ClaimsMappingPoliciesRequest
	from .app_role_assignments import AppRoleAssignmentsRequest
	from .app_role_assigned_to import AppRoleAssignedToRequest
	from .app_management_policies import AppManagementPoliciesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.service_principal import ServicePrincipal
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByServicePrincipalIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ServicePrincipal:
		"""
		Get servicePrincipal
		Retrieve the properties and relationships of a servicePrincipal object.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-get?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.servicePrincipal']

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
		return await self.request_adapter.send_async(request_info, ServicePrincipal, error_mapping)

	async def patch(
		self,
		body: ServicePrincipal,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ServicePrincipal:
		"""
		Upsert servicePrincipal
		Create a new servicePrincipal object if it doesn't exist, or update the properties of an existing servicePrincipal object.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-upsert?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.servicePrincipal']

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
		return await self.request_adapter.send_async(request_info, ServicePrincipal, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete servicePrincipal
		Delete a servicePrincipal object.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-delete?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.servicePrincipal']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	@property
	def app_management_policies(self,
	) -> AppManagementPoliciesRequest:
		from .app_management_policies import AppManagementPoliciesRequest
		return AppManagementPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def app_role_assigned_to(self,
	) -> AppRoleAssignedToRequest:
		from .app_role_assigned_to import AppRoleAssignedToRequest
		return AppRoleAssignedToRequest(self.request_adapter, self.path_parameters)

	@property
	def app_role_assignments(self,
	) -> AppRoleAssignmentsRequest:
		from .app_role_assignments import AppRoleAssignmentsRequest
		return AppRoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def claims_mapping_policies(self,
	) -> ClaimsMappingPoliciesRequest:
		from .claims_mapping_policies import ClaimsMappingPoliciesRequest
		return ClaimsMappingPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def created_objects(self,
	) -> CreatedObjectsRequest:
		from .created_objects import CreatedObjectsRequest
		return CreatedObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def delegated_permission_classifications(self,
	) -> DelegatedPermissionClassificationsRequest:
		from .delegated_permission_classifications import DelegatedPermissionClassificationsRequest
		return DelegatedPermissionClassificationsRequest(self.request_adapter, self.path_parameters)

	@property
	def endpoints(self,
	) -> EndpointsRequest:
		from .endpoints import EndpointsRequest
		return EndpointsRequest(self.request_adapter, self.path_parameters)

	@property
	def federated_identity_credentials(self,
	) -> FederatedIdentityCredentialsRequest:
		from .federated_identity_credentials import FederatedIdentityCredentialsRequest
		return FederatedIdentityCredentialsRequest(self.request_adapter, self.path_parameters)

	@property
	def home_realm_discovery_policies(self,
	) -> HomeRealmDiscoveryPoliciesRequest:
		from .home_realm_discovery_policies import HomeRealmDiscoveryPoliciesRequest
		return HomeRealmDiscoveryPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def member_of(self,
	) -> MemberOfRequest:
		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, self.path_parameters)

	@property
	def add_key(self,
	) -> AddKeyRequest:
		from .add_key import AddKeyRequest
		return AddKeyRequest(self.request_adapter, self.path_parameters)

	@property
	def add_password(self,
	) -> AddPasswordRequest:
		from .add_password import AddPasswordRequest
		return AddPasswordRequest(self.request_adapter, self.path_parameters)

	@property
	def add_token_signing_certificate(self,
	) -> AddTokenSigningCertificateRequest:
		from .add_token_signing_certificate import AddTokenSigningCertificateRequest
		return AddTokenSigningCertificateRequest(self.request_adapter, self.path_parameters)

	@property
	def check_member_groups(self,
	) -> CheckMemberGroupsRequest:
		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def check_member_objects(self,
	) -> CheckMemberObjectsRequest:
		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_member_groups(self,
	) -> GetMemberGroupsRequest:
		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_member_objects(self,
	) -> GetMemberObjectsRequest:
		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def remove_key(self,
	) -> RemoveKeyRequest:
		from .remove_key import RemoveKeyRequest
		return RemoveKeyRequest(self.request_adapter, self.path_parameters)

	@property
	def remove_password(self,
	) -> RemovePasswordRequest:
		from .remove_password import RemovePasswordRequest
		return RemovePasswordRequest(self.request_adapter, self.path_parameters)

	@property
	def restore(self,
	) -> RestoreRequest:
		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def oauth2_permission_grants(self,
	) -> Oauth2PermissionGrantsRequest:
		from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
		return Oauth2PermissionGrantsRequest(self.request_adapter, self.path_parameters)

	@property
	def owned_objects(self,
	) -> OwnedObjectsRequest:
		from .owned_objects import OwnedObjectsRequest
		return OwnedObjectsRequest(self.request_adapter, self.path_parameters)

	@property
	def owners(self,
	) -> OwnersRequest:
		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, self.path_parameters)

	@property
	def remote_desktop_security_configuration(self,
	) -> RemoteDesktopSecurityConfigurationRequest:
		from .remote_desktop_security_configuration import RemoteDesktopSecurityConfigurationRequest
		return RemoteDesktopSecurityConfigurationRequest(self.request_adapter, self.path_parameters)

	@property
	def synchronization(self,
	) -> SynchronizationRequest:
		from .synchronization import SynchronizationRequest
		return SynchronizationRequest(self.request_adapter, self.path_parameters)

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

	@property
	def transitive_member_of(self,
	) -> TransitiveMemberOfRequest:
		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, self.path_parameters)

