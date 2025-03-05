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
	from .count import CountRequest
	from .by_user_experience_analytics_work_from_anywhere_device_id import ByUserExperienceAnalyticsWorkFromAnywhereDeviceIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.user_experience_analytics_work_from_anywhere_device_collection_response import UserExperienceAnalyticsWorkFromAnywhereDeviceCollectionResponse
from iograph_models.models.user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice


class MetricDevicesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsWorkFromAnywhereMetrics/{userExperienceAnalyticsWorkFromAnywhereMetric%2Did}/metricDevices", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsWorkFromAnywhereDeviceCollectionResponse:
		"""
		Get metricDevices from deviceManagement
		The work from anywhere metric devices. Read-only.
		"""
		tags = ['deviceManagement.userExperienceAnalyticsWorkFromAnywhereMetric']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsWorkFromAnywhereDeviceCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserExperienceAnalyticsWorkFromAnywhereDevice,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsWorkFromAnywhereDevice:
		"""
		Create new navigation property to metricDevices for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsWorkFromAnywhereMetric']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsWorkFromAnywhereDevice, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MetricDevicesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MetricDevicesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MetricDevicesRequest(self.request_adapter, self.path_parameters)

	def by_user_experience_analytics_work_from_anywhere_device_id(self,
		userExperienceAnalyticsWorkFromAnywhereMetric_id: str,
		userExperienceAnalyticsWorkFromAnywhereDevice_id: str,
	) -> ByUserExperienceAnalyticsWorkFromAnywhereDeviceIdRequest:
		if userExperienceAnalyticsWorkFromAnywhereMetric_id is None:
			raise TypeError("userExperienceAnalyticsWorkFromAnywhereMetric_id cannot be null.")
		if userExperienceAnalyticsWorkFromAnywhereDevice_id is None:
			raise TypeError("userExperienceAnalyticsWorkFromAnywhereDevice_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsWorkFromAnywhereMetric%2Did"] =  userExperienceAnalyticsWorkFromAnywhereMetric_id
		path_parameters["userExperienceAnalyticsWorkFromAnywhereDevice%2Did"] =  userExperienceAnalyticsWorkFromAnywhereDevice_id

		from .by_user_experience_analytics_work_from_anywhere_device_id import ByUserExperienceAnalyticsWorkFromAnywhereDeviceIdRequest
		return ByUserExperienceAnalyticsWorkFromAnywhereDeviceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		userExperienceAnalyticsWorkFromAnywhereMetric_id: str,
	) -> CountRequest:
		if userExperienceAnalyticsWorkFromAnywhereMetric_id is None:
			raise TypeError("userExperienceAnalyticsWorkFromAnywhereMetric_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsWorkFromAnywhereMetric%2Did"] =  userExperienceAnalyticsWorkFromAnywhereMetric_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

