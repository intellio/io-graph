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
	from .count import CountRequest
	from .by_b2x_identity_user_flow_id import ByB2xIdentityUserFlowIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.b2x_identity_user_flow_collection_response import B2xIdentityUserFlowCollectionResponse
from iograph_models.v1.b2x_identity_user_flow import B2xIdentityUserFlow
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class B2xUserFlowsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identity/b2xUserFlows", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> B2xIdentityUserFlowCollectionResponse:
		"""
		List b2xIdentityUserFlows
		Retrieve a list of b2xIdentityUserFlow objects.
		Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-list-b2xuserflows?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, B2xIdentityUserFlowCollectionResponse, error_mapping)

	async def post(
		self,
		body: B2xIdentityUserFlow,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> B2xIdentityUserFlow:
		"""
		Create b2xIdentityUserFlow
		Create a new b2xIdentityUserFlow object.
		Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-post-b2xuserflows?view=graph-rest-1.0
		"""
		tags = ['identity.b2xIdentityUserFlow']

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
		return await self.request_adapter.send_async(request_info, B2xIdentityUserFlow, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> B2xUserFlowsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: B2xUserFlowsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return B2xUserFlowsRequest(self.request_adapter, self.path_parameters)

	def by_b2x_identity_user_flow_id(self,
		b2xIdentityUserFlow_id: str,
	) -> ByB2xIdentityUserFlowIdRequest:
		if b2xIdentityUserFlow_id is None:
			raise TypeError("b2xIdentityUserFlow_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["b2xIdentityUserFlow%2Did"] =  b2xIdentityUserFlow_id

		from .by_b2x_identity_user_flow_id import ByB2xIdentityUserFlowIdRequest
		return ByB2xIdentityUserFlowIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

