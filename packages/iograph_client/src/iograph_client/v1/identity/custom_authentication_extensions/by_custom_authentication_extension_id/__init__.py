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
	from .validate_authentication_configuration import ValidateAuthenticationConfigurationRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.custom_authentication_extension import CustomAuthenticationExtension


class ByCustomAuthenticationExtensionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/customAuthenticationExtensions/{customAuthenticationExtension%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> CustomAuthenticationExtension:
		"""
		Get customAuthenticationExtension
		Read the properties and relationships of a customAuthenticationExtension object. The following derived types are currently supported.
		Find more info here: https://learn.microsoft.com/graph/api/customauthenticationextension-get?view=graph-rest-1.0
		"""
		tags = ['identity.customAuthenticationExtension']

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
		return await self.request_adapter.send_async(request_info, CustomAuthenticationExtension, error_mapping)

	async def patch(
		self,
		body: CustomAuthenticationExtension,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> CustomAuthenticationExtension:
		"""
		Update customAuthenticationExtension
		Update the properties of a customAuthenticationExtension object. The following derived types are currently supported.
		Find more info here: https://learn.microsoft.com/graph/api/customauthenticationextension-update?view=graph-rest-1.0
		"""
		tags = ['identity.customAuthenticationExtension']

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
		return await self.request_adapter.send_async(request_info, CustomAuthenticationExtension, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete customAuthenticationExtension
		Delete a customAuthenticationExtension object. The following derived types are currently supported.
		Find more info here: https://learn.microsoft.com/graph/api/customauthenticationextension-delete?view=graph-rest-1.0
		"""
		tags = ['identity.customAuthenticationExtension']
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



	def with_url(self, raw_url: str) -> ByCustomAuthenticationExtensionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByCustomAuthenticationExtensionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByCustomAuthenticationExtensionIdRequest(self.request_adapter, self.path_parameters)

	def validate_authentication_configuration(self,
		customAuthenticationExtension_id: str,
	) -> ValidateAuthenticationConfigurationRequest:
		if customAuthenticationExtension_id is None:
			raise TypeError("customAuthenticationExtension_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["customAuthenticationExtension%2Did"] =  customAuthenticationExtension_id

		from .validate_authentication_configuration import ValidateAuthenticationConfigurationRequest
		return ValidateAuthenticationConfigurationRequest(self.request_adapter, path_parameters)

