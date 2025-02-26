# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_external_users_self_service_sign_up_events_flow import GraphExternalUsersSelfServiceSignUpEventsFlowRequest
	from .conditions import ConditionsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.authentication_events_flow import AuthenticationEventsFlow


class ByAuthenticationEventsFlowIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AuthenticationEventsFlow:
		"""
		Get authenticationEventsFlow
		Retrieve the properties and relationships of a specific authenticationEventsFlow object by ID. The @odata.type property in the response object indicates the type of the object, which can be one of the following derived subtypes:
- externalUsersSelfServiceSignupEventsFlow
		Find more info here: https://learn.microsoft.com/graph/api/authenticationeventsflow-get?view=graph-rest-1.0
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
		Find more info here: https://learn.microsoft.com/graph/api/authenticationeventsflow-update?view=graph-rest-1.0
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
		Delete a specific authenticationEventsFlow resource by ID. This operation also removes or unlinks all applications from the flow, which disables the customized authentication experience defined for the application.  The following derived subtypes are supported:
- externalUsersSelfServiceSignupEventsFlow
		Find more info here: https://learn.microsoft.com/graph/api/authenticationeventsflow-delete?view=graph-rest-1.0
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



	@property
	def conditions(self,
	) -> ConditionsRequest:
		from .conditions import ConditionsRequest
		return ConditionsRequest(self.request_adapter, self.path_parameters)

	@property
	def graph_external_users_self_service_sign_up_events_flow(self,
	) -> GraphExternalUsersSelfServiceSignUpEventsFlowRequest:
		from .graph_external_users_self_service_sign_up_events_flow import GraphExternalUsersSelfServiceSignUpEventsFlowRequest
		return GraphExternalUsersSelfServiceSignUpEventsFlowRequest(self.request_adapter, self.path_parameters)

