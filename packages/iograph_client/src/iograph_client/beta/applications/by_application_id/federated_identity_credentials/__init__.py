# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_federated_identity_credential_id import ByFederatedIdentityCredentialIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.federated_identity_credential_collection_response import FederatedIdentityCredentialCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.federated_identity_credential import FederatedIdentityCredential


class FederatedIdentityCredentialsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/federatedIdentityCredentials", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> FederatedIdentityCredentialCollectionResponse:
		"""
		List federatedIdentityCredentials
		Get a list of the federatedIdentityCredential objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/application-list-federatedidentitycredentials?view=graph-rest-beta
		"""
		tags = ['applications.federatedIdentityCredential']

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
		return await self.request_adapter.send_async(request_info, FederatedIdentityCredentialCollectionResponse, error_mapping)

	async def post(
		self,
		body: FederatedIdentityCredential,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> FederatedIdentityCredential:
		"""
		Create federatedIdentityCredential
		Create a new federatedIdentityCredential object for an application. By configuring a trust relationship between your Microsoft Entra application registration and the identity provider for your compute platform, you can use tokens issued by that platform to authenticate with Microsoft identity platform and call APIs in the Microsoft ecosystem. Maximum of 20 objects can be added to an application.
		Find more info here: https://learn.microsoft.com/graph/api/application-post-federatedidentitycredentials?view=graph-rest-beta
		"""
		tags = ['applications.federatedIdentityCredential']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, FederatedIdentityCredential, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> FederatedIdentityCredentialsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FederatedIdentityCredentialsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FederatedIdentityCredentialsRequest(self.request_adapter, self.path_parameters)

	def by_federated_identity_credential_id(self,
		application_id: str,
		federatedIdentityCredential_id: str,
	) -> ByFederatedIdentityCredentialIdRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")
		if federatedIdentityCredential_id is None:
			raise TypeError("federatedIdentityCredential_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id
		path_parameters["federatedIdentityCredential%2Did"] =  federatedIdentityCredential_id

		from .by_federated_identity_credential_id import ByFederatedIdentityCredentialIdRequest
		return ByFederatedIdentityCredentialIdRequest(self.request_adapter, path_parameters)

	def count(self,
		application_id: str,
	) -> CountRequest:
		if application_id is None:
			raise TypeError("application_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["application%2Did"] =  application_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

