# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .on_authentication_method_load_start import OnAuthenticationMethodLoadStartRequest
	from .on_attribute_collection import OnAttributeCollectionRequest
	from .conditions import ConditionsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow


class GraphExternalUsersSelfServiceSignUpEventsFlowRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExternalUsersSelfServiceSignUpEventsFlow:
		"""
		Get the item of type microsoft.graph.authenticationEventsFlow as microsoft.graph.externalUsersSelfServiceSignUpEventsFlow
		
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
		return await self.request_adapter.send_async(request_info, ExternalUsersSelfServiceSignUpEventsFlow, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	@property
	def conditions(self,
	) -> ConditionsRequest:
		from .conditions import ConditionsRequest
		return ConditionsRequest(self.request_adapter, self.path_parameters)

	@property
	def on_attribute_collection(self,
	) -> OnAttributeCollectionRequest:
		from .on_attribute_collection import OnAttributeCollectionRequest
		return OnAttributeCollectionRequest(self.request_adapter, self.path_parameters)

	@property
	def on_authentication_method_load_start(self,
	) -> OnAuthenticationMethodLoadStartRequest:
		from .on_authentication_method_load_start import OnAuthenticationMethodLoadStartRequest
		return OnAuthenticationMethodLoadStartRequest(self.request_adapter, self.path_parameters)

