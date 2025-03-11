# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .post_federation_signup import PostFederationSignupRequest
	from .post_attribute_collection import PostAttributeCollectionRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration


class ApiConnectorConfigurationRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/apiConnectorConfiguration", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserFlowApiConnectorConfiguration:
		"""
		Get userFlowApiConnectorConfiguration
		Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.
		Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-get-apiconnectorconfiguration?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, UserFlowApiConnectorConfiguration, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ApiConnectorConfigurationRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ApiConnectorConfigurationRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ApiConnectorConfigurationRequest(self.request_adapter, self.path_parameters)

	def post_attribute_collection(self,
		b2xIdentityUserFlow_id: str,
	) -> PostAttributeCollectionRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .post_attribute_collection import PostAttributeCollectionRequest
		return PostAttributeCollectionRequest(self.request_adapter, path_parameters)

	def post_federation_signup(self,
		b2xIdentityUserFlow_id: str,
	) -> PostFederationSignupRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .post_federation_signup import PostFederationSignupRequest
		return PostFederationSignupRequest(self.request_adapter, path_parameters)

