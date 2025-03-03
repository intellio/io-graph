# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_on_authentication_method_load_start_external_users_self_service_sign_up import GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class OnAuthenticationMethodLoadStartRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnAuthenticationMethodLoadStartHandler:
		"""
		Get onAuthenticationMethodLoadStart property value
		Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.  Supports $filter (eq). See support for filtering on user flows for syntax information.
		"""
		tags = ['identity.authenticationEventsFlow']

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
		return await self.request_adapter.send_async(request_info, OnAuthenticationMethodLoadStartHandler, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> OnAuthenticationMethodLoadStartRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OnAuthenticationMethodLoadStartRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OnAuthenticationMethodLoadStartRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_on_authentication_method_load_start_external_users_self_service_sign_up(self,
	) -> GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest:
		from .graph_on_authentication_method_load_start_external_users_self_service_sign_up import GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest
		return GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest(self.request_adapter, self.path_parameters)

