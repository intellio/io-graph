# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.federated_identity_credential import FederatedIdentityCredential


class ByFederatedIdentityCredentialIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/federatedIdentityCredentials/{federatedIdentityCredential%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> FederatedIdentityCredential:
		"""
		Get federatedIdentityCredential
		Read the properties and relationships of a federatedIdentityCredential object.
		Find more info here: https://learn.microsoft.com/graph/api/federatedidentitycredential-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, FederatedIdentityCredential, error_mapping)

	async def patch(
		self,
		body: FederatedIdentityCredential,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> FederatedIdentityCredential:
		"""
		Upsert federatedIdentityCredential
		Create a new federatedIdentityCredential object for an application if it doesn't exist, or update the properties of an existing federatedIdentityCredential object. By configuring a trust relationship between your Microsoft Entra application registration and the identity provider for your compute platform, you can use tokens issued by that platform to authenticate with Microsoft identity platform and call APIs in the Microsoft ecosystem. Maximum of 20 objects can be added to an application.
		Find more info here: https://learn.microsoft.com/graph/api/federatedidentitycredential-upsert?view=graph-rest-beta
		"""
		tags = ['applications.federatedIdentityCredential']

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
		return await self.request_adapter.send_async(request_info, FederatedIdentityCredential, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete federatedIdentityCredential
		Deletes a federatedIdentityCredential object from an application.
		Find more info here: https://learn.microsoft.com/graph/api/federatedidentitycredential-delete?view=graph-rest-beta
		"""
		tags = ['applications.federatedIdentityCredential']
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



	def with_url(self, raw_url: str) -> ByFederatedIdentityCredentialIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByFederatedIdentityCredentialIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByFederatedIdentityCredentialIdRequest(self.request_adapter, self.path_parameters)

