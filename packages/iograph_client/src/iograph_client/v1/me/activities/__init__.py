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
	from .recent import RecentRequest
	from .count import CountRequest
	from .by_user_activity_id import ByUserActivityIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.user_activity_collection_response import UserActivityCollectionResponse
from iograph_models.v1.user_activity import UserActivity
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ActivitiesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/activities", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserActivityCollectionResponse:
		"""
		Get user activities
		Get activities for a given user. Unlike the recent OData function, activities without histories will be returned. The permission UserActivity.ReadWrite.CreatedByApp will apply extra filtering to the response, so that only activities created by your application are returned. This server-side filtering might result in empty pages if the user is particularly active and other applications have created more recent activities. To get your application's activities, use the nextLink property to paginate.
		Find more info here: https://learn.microsoft.com/graph/api/projectrome-get-activities?view=graph-rest-1.0
		"""
		tags = ['me.userActivity']

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
		return await self.request_adapter.send_async(request_info, UserActivityCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserActivity,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserActivity:
		"""
		Create new navigation property to activities for me
		
		"""
		tags = ['me.userActivity']

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
		return await self.request_adapter.send_async(request_info, UserActivity, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ActivitiesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ActivitiesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ActivitiesRequest(self.request_adapter, self.path_parameters)

	def by_user_activity_id(self,
		userActivity_id: str,
	) -> ByUserActivityIdRequest:
		if userActivity_id is None:
			raise TypeError("userActivity_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userActivity%2Did"] =  userActivity_id

		from .by_user_activity_id import ByUserActivityIdRequest
		return ByUserActivityIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def recent(self,
	) -> RecentRequest:
		from .recent import RecentRequest
		return RecentRequest(self.request_adapter, self.path_parameters)

