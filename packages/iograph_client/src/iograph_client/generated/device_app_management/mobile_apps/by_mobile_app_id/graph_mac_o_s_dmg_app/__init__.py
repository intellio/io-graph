# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .content_versions import ContentVersionsRequest
	from .categories import CategoriesRequest
	from .assignments import AssignmentsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.mac_o_s_dmg_app import MacOSDmgApp
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class GraphMacOSDmgAppRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}/graph.macOSDmgApp", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MacOSDmgApp:
		"""
		Get the item of type microsoft.graph.mobileApp as microsoft.graph.macOSDmgApp
		
		"""
		tags = ['deviceAppManagement.mobileApp']

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
		return await self.request_adapter.send_async(request_info, MacOSDmgApp, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> GraphMacOSDmgAppRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GraphMacOSDmgAppRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GraphMacOSDmgAppRequest(self.request_adapter, self.path_parameters)

	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def categories(self,
	) -> CategoriesRequest:
		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def content_versions(self,
	) -> ContentVersionsRequest:
		from .content_versions import ContentVersionsRequest
		return ContentVersionsRequest(self.request_adapter, self.path_parameters)

