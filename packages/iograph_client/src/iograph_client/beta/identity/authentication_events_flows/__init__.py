# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_external_users_self_service_sign_up_events_flow import GraphExternalUsersSelfServiceSignUpEventsFlowRequest
	from .count import CountRequest
	from .by_authentication_events_flow_id import ByAuthenticationEventsFlowIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.authentication_events_flow import AuthenticationEventsFlow
from iograph_models.beta.authentication_events_flow_collection_response import AuthenticationEventsFlowCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AuthenticationEventsFlowsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationEventsFlowCollectionResponse:
		"""
		List authenticationEventsFlows
		Get a collection of authentication events policies that are derived from authenticationEventsFlow. Only the externalUsersSelfServiceSignupEventsFlow object type is returned.
		Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-list-authenticationeventsflows?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, AuthenticationEventsFlowCollectionResponse, error_mapping)

	async def post(
		self,
		body: AuthenticationEventsFlow,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationEventsFlow:
		"""
		Create authenticationEventsFlow
		Create a new authenticationEventsFlow object that is of the type specified in the request body. You can create only an externalUsersSelfServiceSignupEventsFlow object type.
		Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-post-authenticationeventsflows?view=graph-rest-beta
		"""
		tags = ['identity.authenticationEventsFlow']

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
		return await self.request_adapter.send_async(request_info, AuthenticationEventsFlow, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AuthenticationEventsFlowsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AuthenticationEventsFlowsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AuthenticationEventsFlowsRequest(self.request_adapter, self.path_parameters)

	def by_authentication_events_flow_id(self,
		authenticationEventsFlow_id: str,
	) -> ByAuthenticationEventsFlowIdRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id

		from .by_authentication_events_flow_id import ByAuthenticationEventsFlowIdRequest
		return ByAuthenticationEventsFlowIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_external_users_self_service_sign_up_events_flow(self,
	) -> GraphExternalUsersSelfServiceSignUpEventsFlowRequest:
		from .graph_external_users_self_service_sign_up_events_flow import GraphExternalUsersSelfServiceSignUpEventsFlowRequest
		return GraphExternalUsersSelfServiceSignUpEventsFlowRequest(self.request_adapter, self.path_parameters)

