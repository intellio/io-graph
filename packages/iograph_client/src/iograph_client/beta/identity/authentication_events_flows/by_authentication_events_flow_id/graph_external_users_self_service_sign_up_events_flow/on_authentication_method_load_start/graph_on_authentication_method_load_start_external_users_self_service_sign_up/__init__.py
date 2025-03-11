# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .identity_providers import IdentityProvidersRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.on_authentication_method_load_start_external_users_self_service_sign_up import OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart/graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp:
		"""
		Get the item of type microsoft.graph.onAuthenticationMethodLoadStartHandler as microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
		
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
		return await self.request_adapter.send_async(request_info, OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp, error_mapping)


	def with_url(self, raw_url: str) -> GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest(self.request_adapter, self.path_parameters)

	def identity_providers(self,
		authenticationEventsFlow_id: str,
	) -> IdentityProvidersRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id

		from .identity_providers import IdentityProvidersRequest
		return IdentityProvidersRequest(self.request_adapter, path_parameters)

