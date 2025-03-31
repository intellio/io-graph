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
	from .by_user_experience_analytics_device_timeline_event_id import ByUserExperienceAnalyticsDeviceTimelineEventIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.user_experience_analytics_device_timeline_event_collection_response import UserExperienceAnalyticsDeviceTimelineEventCollectionResponse
from iograph_models.beta.user_experience_analytics_device_timeline_event import UserExperienceAnalyticsDeviceTimelineEvent
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class UserExperienceAnalyticsDeviceTimelineEventRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsDeviceTimelineEvent", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsDeviceTimelineEventCollectionResponse:
		"""
		Get userExperienceAnalyticsDeviceTimelineEvent from deviceManagement
		The user experience analytics device events entity contains NRT device timeline event details.
		"""
		tags = ['deviceManagement.userExperienceAnalyticsDeviceTimelineEvent']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsDeviceTimelineEventCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserExperienceAnalyticsDeviceTimelineEvent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsDeviceTimelineEvent:
		"""
		Create new navigation property to userExperienceAnalyticsDeviceTimelineEvent for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsDeviceTimelineEvent']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsDeviceTimelineEvent, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserExperienceAnalyticsDeviceTimelineEventRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserExperienceAnalyticsDeviceTimelineEventRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserExperienceAnalyticsDeviceTimelineEventRequest(self.request_adapter, self.path_parameters)

	def by_user_experience_analytics_device_timeline_event_id(self,
		userExperienceAnalyticsDeviceTimelineEvent_id: str,
	) -> ByUserExperienceAnalyticsDeviceTimelineEventIdRequest:
		if userExperienceAnalyticsDeviceTimelineEvent_id is None:
			raise TypeError("userExperienceAnalyticsDeviceTimelineEvent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsDeviceTimelineEvent%2Did"] =  userExperienceAnalyticsDeviceTimelineEvent_id

		from .by_user_experience_analytics_device_timeline_event_id import ByUserExperienceAnalyticsDeviceTimelineEventIdRequest
		return ByUserExperienceAnalyticsDeviceTimelineEventIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

