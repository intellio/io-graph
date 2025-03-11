# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.authentication_configuration_validation import AuthenticationConfigurationValidation
from iograph_models.v1.validate_authentication_configuration_post_request import Validate_authentication_configurationPostRequest


class ValidateAuthenticationConfigurationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/customAuthenticationExtensions/validateAuthenticationConfiguration", path_parameters)

	async def post(
		self,
		body: Validate_authentication_configurationPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationConfigurationValidation:
		"""
		Invoke action validateAuthenticationConfiguration
		
		"""
		tags = ['identity.customAuthenticationExtension']

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
		return await self.request_adapter.send_async(request_info, AuthenticationConfigurationValidation, error_mapping)


	def with_url(self, raw_url: str) -> ValidateAuthenticationConfigurationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ValidateAuthenticationConfigurationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ValidateAuthenticationConfigurationRequest(self.request_adapter, self.path_parameters)

