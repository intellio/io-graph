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
	from .count import CountRequest
	from .by_post_id import ByPostIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.post_collection_response import PostCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class PostsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/threads/{conversationThread%2Did}/posts", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PostCollectionResponse:
		"""
		Get post
		Get the properties and relationships of a post in a specified thread. You can specify both the parent 
conversation and the thread, or, you can specify the thread without referencing the parent conversation. Since the post resource supports extensions, you can also use the GET operation to get custom properties and extension data in a post instance.
		Find more info here: https://learn.microsoft.com/graph/api/post-get?view=graph-rest-1.0
		"""
		tags = ['groups.conversationThread']

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
		return await self.request_adapter.send_async(request_info, PostCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> PostsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PostsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PostsRequest(self.request_adapter, self.path_parameters)

	def by_post_id(self,
		group_id: str,
		conversationThread_id: str,
		post_id: str,
	) -> ByPostIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id

		from .by_post_id import ByPostIdRequest
		return ByPostIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

