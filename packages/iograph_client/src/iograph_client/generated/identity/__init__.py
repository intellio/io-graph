# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .user_flow_attributes import UserFlowAttributesRequest
	from .identity_providers import IdentityProvidersRequest
	from .custom_authentication_extensions import CustomAuthenticationExtensionsRequest
	from .conditional_access import ConditionalAccessRequest
	from .b2x_user_flows import B2xUserFlowsRequest
	from .authentication_events_flows import AuthenticationEventsFlowsRequest
	from .authentication_event_listeners import AuthenticationEventListenersRequest
	from .api_connectors import ApiConnectorsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.identity_container import IdentityContainer


class IdentityRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IdentityContainer:
		"""
		Get identity
		
		"""
		tags = ['identity.identityContainer']

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
		return await self.request_adapter.send_async(request_info, IdentityContainer, error_mapping)

	async def patch(
		self,
		body: IdentityContainer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> IdentityContainer:
		"""
		Update identity
		
		"""
		tags = ['identity.identityContainer']

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
		return await self.request_adapter.send_async(request_info, IdentityContainer, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> IdentityRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: IdentityRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return IdentityRequest(self.request_adapter, self.path_parameters)

	@property
	def api_connectors(self,
	) -> ApiConnectorsRequest:
		from .api_connectors import ApiConnectorsRequest
		return ApiConnectorsRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_event_listeners(self,
	) -> AuthenticationEventListenersRequest:
		from .authentication_event_listeners import AuthenticationEventListenersRequest
		return AuthenticationEventListenersRequest(self.request_adapter, self.path_parameters)

	@property
	def authentication_events_flows(self,
	) -> AuthenticationEventsFlowsRequest:
		from .authentication_events_flows import AuthenticationEventsFlowsRequest
		return AuthenticationEventsFlowsRequest(self.request_adapter, self.path_parameters)

	@property
	def b2x_user_flows(self,
	) -> B2xUserFlowsRequest:
		from .b2x_user_flows import B2xUserFlowsRequest
		return B2xUserFlowsRequest(self.request_adapter, self.path_parameters)

	@property
	def conditional_access(self,
	) -> ConditionalAccessRequest:
		from .conditional_access import ConditionalAccessRequest
		return ConditionalAccessRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_authentication_extensions(self,
	) -> CustomAuthenticationExtensionsRequest:
		from .custom_authentication_extensions import CustomAuthenticationExtensionsRequest
		return CustomAuthenticationExtensionsRequest(self.request_adapter, self.path_parameters)

	@property
	def identity_providers(self,
	) -> IdentityProvidersRequest:
		from .identity_providers import IdentityProvidersRequest
		return IdentityProvidersRequest(self.request_adapter, self.path_parameters)

	@property
	def user_flow_attributes(self,
	) -> UserFlowAttributesRequest:
		from .user_flow_attributes import UserFlowAttributesRequest
		return UserFlowAttributesRequest(self.request_adapter, self.path_parameters)

