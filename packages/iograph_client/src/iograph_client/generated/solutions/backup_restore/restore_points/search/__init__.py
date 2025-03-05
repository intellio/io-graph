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
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.search_post_request import SearchPostRequest
from iograph_models.models.restore_point_search_response import RestorePointSearchResponse


class SearchRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/restorePoints/search", path_parameters)

	async def post(
		self,
		body: SearchPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RestorePointSearchResponse:
		"""
		Invoke action search
		Search for the restorePoint objects associated with a protectionUnit.
		Find more info here: https://learn.microsoft.com/graph/api/restorepoint-search?view=graph-rest-1.0
		"""
		tags = ['solutions.backupRestoreRoot']

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
		return await self.request_adapter.send_async(request_info, RestorePointSearchResponse, error_mapping)


	def with_url(self, raw_url: str) -> SearchRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SearchRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SearchRequest(self.request_adapter, self.path_parameters)

