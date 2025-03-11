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
	from .relationships import RelationshipsRequest
	from .categories import CategoriesRequest
	from .assignments import AssignmentsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.android_for_work_app import AndroidForWorkApp


class GraphAndroidForWorkAppRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}/graph.androidForWorkApp", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AndroidForWorkApp:
		"""
		Get the item of type microsoft.graph.mobileApp as microsoft.graph.androidForWorkApp
		
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
		return await self.request_adapter.send_async(request_info, AndroidForWorkApp, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> GraphAndroidForWorkAppRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GraphAndroidForWorkAppRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GraphAndroidForWorkAppRequest(self.request_adapter, self.path_parameters)

	def assignments(self,
		mobileApp_id: str,
	) -> AssignmentsRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id

		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, path_parameters)

	def categories(self,
		mobileApp_id: str,
	) -> CategoriesRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id

		from .categories import CategoriesRequest
		return CategoriesRequest(self.request_adapter, path_parameters)

	def relationships(self,
		mobileApp_id: str,
	) -> RelationshipsRequest:
		if mobileApp_id is None:
			raise TypeError("mobileApp_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mobileApp%2Did"] =  mobileApp_id

		from .relationships import RelationshipsRequest
		return RelationshipsRequest(self.request_adapter, path_parameters)

