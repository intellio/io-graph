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
	from .count import CountRequest
	from .by_shared_insight_id import BySharedInsightIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.shared_insight import SharedInsight
from iograph_models.v1.shared_insight_collection_response import SharedInsightCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class SharedRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/insights/shared", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SharedInsightCollectionResponse:
		"""
		List shared
		Calculated insight that includes the list of documents shared with a user. This insight includes documents hosted on OneDrive/SharePoint in the user's Microsoft 365 tenant that are shared with the user, and documents that are attached as files and sent to the user.
		Find more info here: https://learn.microsoft.com/graph/api/insights-list-shared?view=graph-rest-1.0
		"""
		tags = ['me.itemInsights']

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
		return await self.request_adapter.send_async(request_info, SharedInsightCollectionResponse, error_mapping)

	async def post(
		self,
		body: SharedInsight,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> SharedInsight:
		"""
		Create new navigation property to shared for me
		
		"""
		tags = ['me.itemInsights']

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
		return await self.request_adapter.send_async(request_info, SharedInsight, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SharedRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SharedRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SharedRequest(self.request_adapter, self.path_parameters)

	def by_shared_insight_id(self,
		sharedInsight_id: str,
	) -> BySharedInsightIdRequest:
		if sharedInsight_id is None:
			raise TypeError("sharedInsight_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedInsight%2Did"] =  sharedInsight_id

		from .by_shared_insight_id import BySharedInsightIdRequest
		return BySharedInsightIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

