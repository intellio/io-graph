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
	from .work_from_anywhere_metrics import WorkFromAnywhereMetricsRequest
	from .resource_performance_metrics import ResourcePerformanceMetricsRequest
	from .reboot_analytics_metrics import RebootAnalyticsMetricsRequest
	from .device_boot_performance_metrics import DeviceBootPerformanceMetricsRequest
	from .best_practices_metrics import BestPracticesMetricsRequest
	from .battery_health_metrics import BatteryHealthMetricsRequest
	from .app_health_metrics import AppHealthMetricsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.user_experience_analytics_baseline import UserExperienceAnalyticsBaseline


class ByUserExperienceAnalyticsBaselineIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsBaselines/{userExperienceAnalyticsBaseline%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsBaseline:
		"""
		Get userExperienceAnalyticsBaselines from deviceManagement
		User experience analytics baselines
		"""
		tags = ['deviceManagement.userExperienceAnalyticsBaseline']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsBaseline, error_mapping)

	async def patch(
		self,
		body: UserExperienceAnalyticsBaseline,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsBaseline:
		"""
		Update the navigation property userExperienceAnalyticsBaselines in deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsBaseline']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsBaseline, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property userExperienceAnalyticsBaselines for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsBaseline']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> ByUserExperienceAnalyticsBaselineIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserExperienceAnalyticsBaselineIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserExperienceAnalyticsBaselineIdRequest(self.request_adapter, self.path_parameters)

	def app_health_metrics(self,
		userExperienceAnalyticsBaseline_id: str,
	) -> AppHealthMetricsRequest:
		if userExperienceAnalyticsBaseline_id is None:
			raise TypeError("userExperienceAnalyticsBaseline_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBaseline%2Did"] =  userExperienceAnalyticsBaseline_id

		from .app_health_metrics import AppHealthMetricsRequest
		return AppHealthMetricsRequest(self.request_adapter, path_parameters)

	def battery_health_metrics(self,
		userExperienceAnalyticsBaseline_id: str,
	) -> BatteryHealthMetricsRequest:
		if userExperienceAnalyticsBaseline_id is None:
			raise TypeError("userExperienceAnalyticsBaseline_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBaseline%2Did"] =  userExperienceAnalyticsBaseline_id

		from .battery_health_metrics import BatteryHealthMetricsRequest
		return BatteryHealthMetricsRequest(self.request_adapter, path_parameters)

	def best_practices_metrics(self,
		userExperienceAnalyticsBaseline_id: str,
	) -> BestPracticesMetricsRequest:
		if userExperienceAnalyticsBaseline_id is None:
			raise TypeError("userExperienceAnalyticsBaseline_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBaseline%2Did"] =  userExperienceAnalyticsBaseline_id

		from .best_practices_metrics import BestPracticesMetricsRequest
		return BestPracticesMetricsRequest(self.request_adapter, path_parameters)

	def device_boot_performance_metrics(self,
		userExperienceAnalyticsBaseline_id: str,
	) -> DeviceBootPerformanceMetricsRequest:
		if userExperienceAnalyticsBaseline_id is None:
			raise TypeError("userExperienceAnalyticsBaseline_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBaseline%2Did"] =  userExperienceAnalyticsBaseline_id

		from .device_boot_performance_metrics import DeviceBootPerformanceMetricsRequest
		return DeviceBootPerformanceMetricsRequest(self.request_adapter, path_parameters)

	def reboot_analytics_metrics(self,
		userExperienceAnalyticsBaseline_id: str,
	) -> RebootAnalyticsMetricsRequest:
		if userExperienceAnalyticsBaseline_id is None:
			raise TypeError("userExperienceAnalyticsBaseline_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBaseline%2Did"] =  userExperienceAnalyticsBaseline_id

		from .reboot_analytics_metrics import RebootAnalyticsMetricsRequest
		return RebootAnalyticsMetricsRequest(self.request_adapter, path_parameters)

	def resource_performance_metrics(self,
		userExperienceAnalyticsBaseline_id: str,
	) -> ResourcePerformanceMetricsRequest:
		if userExperienceAnalyticsBaseline_id is None:
			raise TypeError("userExperienceAnalyticsBaseline_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBaseline%2Did"] =  userExperienceAnalyticsBaseline_id

		from .resource_performance_metrics import ResourcePerformanceMetricsRequest
		return ResourcePerformanceMetricsRequest(self.request_adapter, path_parameters)

	def work_from_anywhere_metrics(self,
		userExperienceAnalyticsBaseline_id: str,
	) -> WorkFromAnywhereMetricsRequest:
		if userExperienceAnalyticsBaseline_id is None:
			raise TypeError("userExperienceAnalyticsBaseline_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsBaseline%2Did"] =  userExperienceAnalyticsBaseline_id

		from .work_from_anywhere_metrics import WorkFromAnywhereMetricsRequest
		return WorkFromAnywhereMetricsRequest(self.request_adapter, path_parameters)

