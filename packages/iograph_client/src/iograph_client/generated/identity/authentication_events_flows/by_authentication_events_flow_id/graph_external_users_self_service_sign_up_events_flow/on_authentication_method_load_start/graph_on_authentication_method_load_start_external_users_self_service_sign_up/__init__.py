# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .identity_providers import IdentityProvidersRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.on_authentication_method_load_start_external_users_self_service_sign_up import OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart/graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp"
		self.path_parameters: dict[str, Any] = path_parameters

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


	@property
	def identity_providers(self,
	) -> IdentityProvidersRequest:
		from .identity_providers import IdentityProvidersRequest
		return IdentityProvidersRequest(self.request_adapter, self.path_parameters)

