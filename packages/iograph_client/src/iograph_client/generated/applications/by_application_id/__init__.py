# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .token_lifetime_policies import TokenLifetimePoliciesRequest
	from .token_issuance_policies import TokenIssuancePoliciesRequest
	from .synchronization import SynchronizationRequest
	from .owners import OwnersRequest
	from .unset_verified_publisher import UnsetVerifiedPublisherRequest
	from .set_verified_publisher import SetVerifiedPublisherRequest
	from .restore import RestoreRequest
	from .remove_password import RemovePasswordRequest
	from .remove_key import RemoveKeyRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .add_password import AddPasswordRequest
	from .add_key import AddKeyRequest
	from .logo import LogoRequest
	from .home_realm_discovery_policies import HomeRealmDiscoveryPoliciesRequest
	from .federated_identity_credentials import FederatedIdentityCredentialsRequest
	from .extension_properties import ExtensionPropertiesRequest
	from .created_on_behalf_of import CreatedOnBehalfOfRequest
	from .app_management_policies import AppManagementPoliciesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.application import Application


class ByApplicationIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/applications/{application%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Application:
		"""
		Get application
		Get the properties and relationships of an application object.
		Find more info here: https://learn.microsoft.com/graph/api/application-get?view=graph-rest-1.0
		"""
		tags = ['applications.application']

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
		return await self.request_adapter.send_async(request_info, Application, error_mapping)

	async def patch(
		self,
		body: Application,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Application:
		"""
		Upsert application
		Create a new application object if it doesn't exist, or update the properties of an existing application object.
		Find more info here: https://learn.microsoft.com/graph/api/application-upsert?view=graph-rest-1.0
		"""
		tags = ['applications.application']

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
		return await self.request_adapter.send_async(request_info, Application, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete application
		Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted.
		Find more info here: https://learn.microsoft.com/graph/api/application-delete?view=graph-rest-1.0
		"""
		tags = ['applications.application']
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
	def created_on_behalf_of(self,
	) -> CreatedOnBehalfOfRequest:
		from .created_on_behalf_of import CreatedOnBehalfOfRequest
		return CreatedOnBehalfOfRequest(self.request_adapter, self.path_parameters)

	@property
	def extension_properties(self,
	) -> ExtensionPropertiesRequest:
		from .extension_properties import ExtensionPropertiesRequest
		return ExtensionPropertiesRequest(self.request_adapter, self.path_parameters)

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
	def logo(self,
	) -> LogoRequest:
		from .logo import LogoRequest
		return LogoRequest(self.request_adapter, self.path_parameters)

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
	def set_verified_publisher(self,
	) -> SetVerifiedPublisherRequest:
		from .set_verified_publisher import SetVerifiedPublisherRequest
		return SetVerifiedPublisherRequest(self.request_adapter, self.path_parameters)

	@property
	def unset_verified_publisher(self,
	) -> UnsetVerifiedPublisherRequest:
		from .unset_verified_publisher import UnsetVerifiedPublisherRequest
		return UnsetVerifiedPublisherRequest(self.request_adapter, self.path_parameters)

	@property
	def owners(self,
	) -> OwnersRequest:
		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, self.path_parameters)

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

