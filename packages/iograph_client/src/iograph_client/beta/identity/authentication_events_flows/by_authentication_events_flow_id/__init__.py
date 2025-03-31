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
	from .graph_external_users_self_service_sign_up_events_flow import GraphExternalUsersSelfServiceSignUpEventsFlowRequest
	from .conditions import ConditionsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.authentication_events_flow import AuthenticationEventsFlow
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByAuthenticationEventsFlowIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationEventsFlow:
		"""
		Get authenticationEventsFlow
		Retrieve the properties and relationships of a specific authenticationEventsFlow object by ID. Only externalUsersSelfServiceSignupEventsFlow object types are available.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationeventsflow-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, AuthenticationEventsFlow, error_mapping)

	async def patch(
		self,
		body: AuthenticationEventsFlow,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AuthenticationEventsFlow:
		"""
		Update authenticationEventsFlow
		Update the properties of an authenticationEventsFlow object by ID. You must specify the @odata.type property and the value of the authenticationEventsFlow object type to update. The following derived subtypes are supported:
- externalUsersSelfServiceSignupEventsFlow
		Find more info here: https://learn.microsoft.com/graph/api/authenticationeventsflow-update?view=graph-rest-beta
		"""
		tags = ['identity.authenticationEventsFlow']

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
		return await self.request_adapter.send_async(request_info, AuthenticationEventsFlow, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete authenticationEventsFlow
		Delete a specific authenticationEventsFlow resource by ID. Only externalUsersSelfServiceSignupEventsFlow object types are available.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationeventsflow-delete?view=graph-rest-beta
		"""
		tags = ['identity.authenticationEventsFlow']
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



	def with_url(self, raw_url: str) -> ByAuthenticationEventsFlowIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAuthenticationEventsFlowIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAuthenticationEventsFlowIdRequest(self.request_adapter, self.path_parameters)

	def conditions(self,
		authenticationEventsFlow_id: str,
	) -> ConditionsRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id

		from .conditions import ConditionsRequest
		return ConditionsRequest(self.request_adapter, path_parameters)

	def graph_external_users_self_service_sign_up_events_flow(self,
		authenticationEventsFlow_id: str,
	) -> GraphExternalUsersSelfServiceSignUpEventsFlowRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id

		from .graph_external_users_self_service_sign_up_events_flow import GraphExternalUsersSelfServiceSignUpEventsFlowRequest
		return GraphExternalUsersSelfServiceSignUpEventsFlowRequest(self.request_adapter, path_parameters)

