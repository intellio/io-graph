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
	from .federated_identity_credentials_with_name import FederatedIdentityCredentialsWithNameRequest
	from .federated_identity_credentials import FederatedIdentityCredentialsRequest
	from .extension_properties import ExtensionPropertiesRequest
	from .created_on_behalf_of import CreatedOnBehalfOfRequest
	from .app_management_policies import AppManagementPoliciesRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.application import Application


class ByApplicationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}", path_parameters)

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



	def with_url(self, raw_url: str) -> ByApplicationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByApplicationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByApplicationIdRequest(self.request_adapter, self.path_parameters)

	def app_management_policies(self,
		application_id: str,
	) -> AppManagementPoliciesRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .app_management_policies import AppManagementPoliciesRequest
		return AppManagementPoliciesRequest(self.request_adapter, path_parameters)

	def created_on_behalf_of(self,
		application_id: str,
	) -> CreatedOnBehalfOfRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .created_on_behalf_of import CreatedOnBehalfOfRequest
		return CreatedOnBehalfOfRequest(self.request_adapter, path_parameters)

	def extension_properties(self,
		application_id: str,
	) -> ExtensionPropertiesRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .extension_properties import ExtensionPropertiesRequest
		return ExtensionPropertiesRequest(self.request_adapter, path_parameters)

	def federated_identity_credentials(self,
		application_id: str,
	) -> FederatedIdentityCredentialsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .federated_identity_credentials import FederatedIdentityCredentialsRequest
		return FederatedIdentityCredentialsRequest(self.request_adapter, path_parameters)

	def federated_identity_credentials_with_name(self,
		application_id: str,
		name: str,
	) -> FederatedIdentityCredentialsWithNameRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["name"] =  name

		from .federated_identity_credentials_with_name import FederatedIdentityCredentialsWithNameRequest
		return FederatedIdentityCredentialsWithNameRequest(self.request_adapter, path_parameters)

	def home_realm_discovery_policies(self,
		application_id: str,
	) -> HomeRealmDiscoveryPoliciesRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .home_realm_discovery_policies import HomeRealmDiscoveryPoliciesRequest
		return HomeRealmDiscoveryPoliciesRequest(self.request_adapter, path_parameters)

	def logo(self,
		application_id: str,
	) -> LogoRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .logo import LogoRequest
		return LogoRequest(self.request_adapter, path_parameters)

	def add_key(self,
		application_id: str,
	) -> AddKeyRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .add_key import AddKeyRequest
		return AddKeyRequest(self.request_adapter, path_parameters)

	def add_password(self,
		application_id: str,
	) -> AddPasswordRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .add_password import AddPasswordRequest
		return AddPasswordRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		application_id: str,
	) -> CheckMemberGroupsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		application_id: str,
	) -> CheckMemberObjectsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		application_id: str,
	) -> GetMemberGroupsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		application_id: str,
	) -> GetMemberObjectsRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def remove_key(self,
		application_id: str,
	) -> RemoveKeyRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .remove_key import RemoveKeyRequest
		return RemoveKeyRequest(self.request_adapter, path_parameters)

	def remove_password(self,
		application_id: str,
	) -> RemovePasswordRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .remove_password import RemovePasswordRequest
		return RemovePasswordRequest(self.request_adapter, path_parameters)

	def restore(self,
		application_id: str,
	) -> RestoreRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def set_verified_publisher(self,
		application_id: str,
	) -> SetVerifiedPublisherRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .set_verified_publisher import SetVerifiedPublisherRequest
		return SetVerifiedPublisherRequest(self.request_adapter, path_parameters)

	def unset_verified_publisher(self,
		application_id: str,
	) -> UnsetVerifiedPublisherRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .unset_verified_publisher import UnsetVerifiedPublisherRequest
		return UnsetVerifiedPublisherRequest(self.request_adapter, path_parameters)

	def owners(self,
		application_id: str,
	) -> OwnersRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .owners import OwnersRequest
		return OwnersRequest(self.request_adapter, path_parameters)

	def synchronization(self,
		application_id: str,
	) -> SynchronizationRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .synchronization import SynchronizationRequest
		return SynchronizationRequest(self.request_adapter, path_parameters)

	def token_issuance_policies(self,
		application_id: str,
	) -> TokenIssuancePoliciesRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .token_issuance_policies import TokenIssuancePoliciesRequest
		return TokenIssuancePoliciesRequest(self.request_adapter, path_parameters)

	def token_lifetime_policies(self,
		application_id: str,
	) -> TokenLifetimePoliciesRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .token_lifetime_policies import TokenLifetimePoliciesRequest
		return TokenLifetimePoliciesRequest(self.request_adapter, path_parameters)

