# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .graph_on_attribute_collection_external_users_self_service_sign_up import GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.on_attribute_collection_handler import OnAttributeCollectionHandler
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class OnAttributeCollectionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAttributeCollection", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnAttributeCollectionHandler:
		"""
		Get onAttributeCollection property value
		The configuration for what to invoke when attributes are ready to be collected from the user.
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
		return await self.request_adapter.send_async(request_info, OnAttributeCollectionHandler, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> OnAttributeCollectionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OnAttributeCollectionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OnAttributeCollectionRequest(self.request_adapter, self.path_parameters)

	def graph_on_attribute_collection_external_users_self_service_sign_up(self,
		authenticationEventsFlow_id: str,
	) -> GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequest:
		if authenticationEventsFlow_id is None:
			raise TypeError("authenticationEventsFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["authenticationEventsFlow%2Did"] =  authenticationEventsFlow_id

		from .graph_on_attribute_collection_external_users_self_service_sign_up import GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequest
		return GraphOnAttributeCollectionExternalUsersSelfServiceSignUpRequest(self.request_adapter, path_parameters)

