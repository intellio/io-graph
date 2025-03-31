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
	from .policies import PoliciesRequest
	from .authentication_method_modes import AuthenticationMethodModesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.authentication_strength_root import AuthenticationStrengthRoot
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class AuthenticationStrengthRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/conditionalAccess/authenticationStrength", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationStrengthRoot:
		"""
		Get authenticationStrength from identity
		
		"""
		tags = ['identity.conditionalAccessRoot']

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
		return await self.request_adapter.send_async(request_info, AuthenticationStrengthRoot, error_mapping)

	async def patch(
		self,
		body: AuthenticationStrengthRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationStrengthRoot:
		"""
		Update the navigation property authenticationStrength in identity
		
		"""
		tags = ['identity.conditionalAccessRoot']

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
		return await self.request_adapter.send_async(request_info, AuthenticationStrengthRoot, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property authenticationStrength for identity
		
		"""
		tags = ['identity.conditionalAccessRoot']
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



	def with_url(self, raw_url: str) -> AuthenticationStrengthRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AuthenticationStrengthRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AuthenticationStrengthRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_method_modes(self,
	) -> AuthenticationMethodModesRequest:
		from .authentication_method_modes import AuthenticationMethodModesRequest
		return AuthenticationMethodModesRequest(self.request_adapter, self.path_parameters)

	@property
	def policies(self,
	) -> PoliciesRequest:
		from .policies import PoliciesRequest
		return PoliciesRequest(self.request_adapter, self.path_parameters)

