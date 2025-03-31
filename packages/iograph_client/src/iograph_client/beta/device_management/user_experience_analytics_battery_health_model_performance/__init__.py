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
	from .by_user_experience_analytics_battery_health_model_performance_id import ByUserExperienceAnalyticsBatteryHealthModelPerformanceIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.user_experience_analytics_battery_health_model_performance import UserExperienceAnalyticsBatteryHealthModelPerformance
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.user_experience_analytics_battery_health_model_performance_collection_response import UserExperienceAnalyticsBatteryHealthModelPerformanceCollectionResponse


class UserExperienceAnalyticsBatteryHealthModelPerformanceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsBatteryHealthModelPerformance", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsBatteryHealthModelPerformanceCollectionResponse:
		"""
		Get userExperienceAnalyticsBatteryHealthModelPerformance from deviceManagement
		User Experience Analytics Battery Health Model Performance
		"""
		tags = ['deviceManagement.userExperienceAnalyticsBatteryHealthModelPerformance']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsBatteryHealthModelPerformanceCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserExperienceAnalyticsBatteryHealthModelPerformance,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsBatteryHealthModelPerformance:
		"""
		Create new navigation property to userExperienceAnalyticsBatteryHealthModelPerformance for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsBatteryHealthModelPerformance']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsBatteryHealthModelPerformance, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UserExperienceAnalyticsBatteryHealthModelPerformanceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UserExperienceAnalyticsBatteryHealthModelPerformanceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UserExperienceAnalyticsBatteryHealthModelPerformanceRequest(self.request_adapter, self.path_parameters)

	def by_user_experience_analytics_battery_health_model_performance_id(self,
		userExperienceAnalyticsBatteryHealthModelPerformance_id: str,
	) -> ByUserExperienceAnalyticsBatteryHealthModelPerformanceIdRequest:
		if userExperienceAnalyticsBatteryHealthModelPerformance_id is None:
			raise TypeError("userExperienceAnalyticsBatteryHealthModelPerformance_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBatteryHealthModelPerformance%2Did"] =  userExperienceAnalyticsBatteryHealthModelPerformance_id

		from .by_user_experience_analytics_battery_health_model_performance_id import ByUserExperienceAnalyticsBatteryHealthModelPerformanceIdRequest
		return ByUserExperienceAnalyticsBatteryHealthModelPerformanceIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

