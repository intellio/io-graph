# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_user_experience_analytics_app_health_app_performance_by_app_version_device_id_id import ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.user_experience_analytics_app_health_app_performance_by_app_version_device_id_collection_response import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId


class UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdCollectionResponse:
		"""
		Get userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId from deviceManagement
		User experience analytics appHealth Application Performance by App Version Device Id
		"""
		tags = ['deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId:
		"""
		Create new navigation property to userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_user_experience_analytics_app_health_app_performance_by_app_version_device_id_id(self,
		userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId_id: str,
	) -> ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdIdRequest:
		if userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId_id is None:
			raise TypeError("userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId%2Did"] =  userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId_id

		from .by_user_experience_analytics_app_health_app_performance_by_app_version_device_id_id import ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdIdRequest
		return ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceIdIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

