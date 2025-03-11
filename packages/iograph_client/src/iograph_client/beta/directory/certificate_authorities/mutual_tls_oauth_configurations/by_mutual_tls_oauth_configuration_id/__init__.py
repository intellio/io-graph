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
from iograph_models.beta.mutual_tls_oauth_configuration import MutualTlsOauthConfiguration
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMutualTlsOauthConfigurationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/certificateAuthorities/mutualTlsOauthConfigurations/{mutualTlsOauthConfiguration%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MutualTlsOauthConfiguration:
		"""
		Get mutualTlsOauthConfiguration
		Get the properties and relationships of the specified mutualTlsOauthConfiguration resource.
		Find more info here: https://learn.microsoft.com/graph/api/mutualtlsoauthconfiguration-get?view=graph-rest-beta
		"""
		tags = ['directory.certificateAuthorityPath']

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
		return await self.request_adapter.send_async(request_info, MutualTlsOauthConfiguration, error_mapping)

	async def patch(
		self,
		body: MutualTlsOauthConfiguration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MutualTlsOauthConfiguration:
		"""
		Update mutualTlsOauthConfiguration
		Update the specified mutualTlsOauthConfiguration resource. You can only update the following two properties: displayName, certificateAuthority. To update a subset of objects in the certificateAuthorities collection, first get the complete list, make your modifications, and then repost the entire contents of the certificateAuthorities attribute list in the request body. Excluding a subset of objects removes them from the collection.
		Find more info here: https://learn.microsoft.com/graph/api/mutualtlsoauthconfiguration-update?view=graph-rest-beta
		"""
		tags = ['directory.certificateAuthorityPath']

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
		return await self.request_adapter.send_async(request_info, MutualTlsOauthConfiguration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property mutualTlsOauthConfigurations for directory
		
		"""
		tags = ['directory.certificateAuthorityPath']
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



	def with_url(self, raw_url: str) -> ByMutualTlsOauthConfigurationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMutualTlsOauthConfigurationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMutualTlsOauthConfigurationIdRequest(self.request_adapter, self.path_parameters)

