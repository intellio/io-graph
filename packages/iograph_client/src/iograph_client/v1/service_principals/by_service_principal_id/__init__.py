# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
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
	from .federated_identity_credentials_with_name import FederatedIdentityCredentialsWithNameRequest
	from .federated_identity_credentials import FederatedIdentityCredentialsRequest
	from .endpoints import EndpointsRequest
	from .delegated_permission_classifications import DelegatedPermissionClassificationsRequest
	from .created_objects import CreatedObjectsRequest
	from .claims_mapping_policies import ClaimsMappingPoliciesRequest
	from .app_role_assignments import AppRoleAssignmentsRequest
	from .app_role_assigned_to import AppRoleAssignedToRequest
	from .app_management_policies import AppManagementPoliciesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.service_principal import ServicePrincipal
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByServicePrincipalIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}", path_parameters)

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



	def with_url(self, raw_url: str) -> ByServicePrincipalIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByServicePrincipalIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByServicePrincipalIdRequest(self.request_adapter, self.path_parameters)

	def app_management_policies(self,
		servicePrincipal_id: str,
	) -> AppManagementPoliciesRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .app_management_policies import AppManagementPoliciesRequest
		return AppManagementPoliciesRequest(self.request_adapter, path_parameters)

	def app_role_assigned_to(self,
		servicePrincipal_id: str,
	) -> AppRoleAssignedToRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .app_role_assigned_to import AppRoleAssignedToRequest
		return AppRoleAssignedToRequest(self.request_adapter, path_parameters)

	def app_role_assignments(self,
		servicePrincipal_id: str,
	) -> AppRoleAssignmentsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .app_role_assignments import AppRoleAssignmentsRequest
		return AppRoleAssignmentsRequest(self.request_adapter, path_parameters)

	def claims_mapping_policies(self,
		servicePrincipal_id: str,
	) -> ClaimsMappingPoliciesRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .claims_mapping_policies import ClaimsMappingPoliciesRequest
		return ClaimsMappingPoliciesRequest(self.request_adapter, path_parameters)

	def created_objects(self,
		servicePrincipal_id: str,
	) -> CreatedObjectsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .created_objects import CreatedObjectsRequest
		return CreatedObjectsRequest(self.request_adapter, path_parameters)

	def delegated_permission_classifications(self,
		servicePrincipal_id: str,
	) -> DelegatedPermissionClassificationsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .delegated_permission_classifications import DelegatedPermissionClassificationsRequest
		return DelegatedPermissionClassificationsRequest(self.request_adapter, path_parameters)

	def endpoints(self,
		servicePrincipal_id: str,
	) -> EndpointsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .endpoints import EndpointsRequest
		return EndpointsRequest(self.request_adapter, path_parameters)

	def federated_identity_credentials(self,
		servicePrincipal_id: str,
	) -> FederatedIdentityCredentialsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .federated_identity_credentials import FederatedIdentityCredentialsRequest
		return FederatedIdentityCredentialsRequest(self.request_adapter, path_parameters)

	def federated_identity_credentials_with_name(self,
		servicePrincipal_id: str,
		name: str,
	) -> FederatedIdentityCredentialsWithNameRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["name"] =  name

		from .federated_identity_credentials_with_name import FederatedIdentityCredentialsWithNameRequest
		return FederatedIdentityCredentialsWithNameRequest(self.request_adapter, path_parameters)

	def home_realm_discovery_policies(self,
		servicePrincipal_id: str,
	) -> HomeRealmDiscoveryPoliciesRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .home_realm_discovery_policies import HomeRealmDiscoveryPoliciesRequest
		return HomeRealmDiscoveryPoliciesRequest(self.request_adapter, path_parameters)

	def member_of(self,
		servicePrincipal_id: str,
	) -> MemberOfRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .member_of import MemberOfRequest
		return MemberOfRequest(self.request_adapter, path_parameters)

	def add_key(self,
		servicePrincipal_id: str,
	) -> AddKeyRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .add_key import AddKeyRequest
		return AddKeyRequest(self.request_adapter, path_parameters)

	def add_password(self,
		servicePrincipal_id: str,
	) -> AddPasswordRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .add_password import AddPasswordRequest
		return AddPasswordRequest(self.request_adapter, path_parameters)

	def add_token_signing_certificate(self,
		servicePrincipal_id: str,
	) -> AddTokenSigningCertificateRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .add_token_signing_certificate import AddTokenSigningCertificateRequest
		return AddTokenSigningCertificateRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		servicePrincipal_id: str,
	) -> CheckMemberGroupsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		servicePrincipal_id: str,
	) -> CheckMemberObjectsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		servicePrincipal_id: str,
	) -> GetMemberGroupsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		servicePrincipal_id: str,
	) -> GetMemberObjectsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def remove_key(self,
		servicePrincipal_id: str,
	) -> RemoveKeyRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .remove_key import RemoveKeyRequest
		return RemoveKeyRequest(self.request_adapter, path_parameters)

	def remove_password(self,
		servicePrincipal_id: str,
	) -> RemovePasswordRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .remove_password import RemovePasswordRequest
		return RemovePasswordRequest(self.request_adapter, path_parameters)

	def restore(self,
		servicePrincipal_id: str,
	) -> RestoreRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def oauth2_permission_grants(self,
		servicePrincipal_id: str,
	) -> Oauth2PermissionGrantsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .oauth2_permission_grants import Oauth2PermissionGrantsRequest
		return Oauth2PermissionGrantsRequest(self.request_adapter, path_parameters)

	def owned_objects(self,
		servicePrincipal_id: str,
	) -> OwnedObjectsRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .owned_objects import OwnedObjectsRequest
		return OwnedObjectsRequest(self.request_adapter, path_parameters)

	def owners(self,
		servicePrincipal_id: str,
	) -> OwnersRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, path_parameters)

	def remote_desktop_security_configuration(self,
		servicePrincipal_id: str,
	) -> RemoteDesktopSecurityConfigurationRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .remote_desktop_security_configuration import RemoteDesktopSecurityConfigurationRequest
		return RemoteDesktopSecurityConfigurationRequest(self.request_adapter, path_parameters)

	def synchronization(self,
		servicePrincipal_id: str,
	) -> SynchronizationRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .synchronization import SynchronizationRequest
		return SynchronizationRequest(self.request_adapter, path_parameters)

	def token_issuance_policies(self,
		servicePrincipal_id: str,
	) -> TokenIssuancePoliciesRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .token_issuance_policies import TokenIssuancePoliciesRequest
		return TokenIssuancePoliciesRequest(self.request_adapter, path_parameters)

	def token_lifetime_policies(self,
		servicePrincipal_id: str,
	) -> TokenLifetimePoliciesRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .token_lifetime_policies import TokenLifetimePoliciesRequest
		return TokenLifetimePoliciesRequest(self.request_adapter, path_parameters)

	def transitive_member_of(self,
		servicePrincipal_id: str,
	) -> TransitiveMemberOfRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .transitive_member_of import TransitiveMemberOfRequest
		return TransitiveMemberOfRequest(self.request_adapter, path_parameters)

