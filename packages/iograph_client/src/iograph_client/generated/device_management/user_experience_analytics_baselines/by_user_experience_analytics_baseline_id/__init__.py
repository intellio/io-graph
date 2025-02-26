# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
from iograph_models.models.user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserExperienceAnalyticsBaselineIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/deviceManagement/userExperienceAnalyticsBaselines/{userExperienceAnalyticsBaseline%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

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



	@property
	def app_health_metrics(self,
	) -> AppHealthMetricsRequest:
		from .app_health_metrics import AppHealthMetricsRequest
		return AppHealthMetricsRequest(self.request_adapter, self.path_parameters)

	@property
	def battery_health_metrics(self,
	) -> BatteryHealthMetricsRequest:
		from .battery_health_metrics import BatteryHealthMetricsRequest
		return BatteryHealthMetricsRequest(self.request_adapter, self.path_parameters)

	@property
	def best_practices_metrics(self,
	) -> BestPracticesMetricsRequest:
		from .best_practices_metrics import BestPracticesMetricsRequest
		return BestPracticesMetricsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_boot_performance_metrics(self,
	) -> DeviceBootPerformanceMetricsRequest:
		from .device_boot_performance_metrics import DeviceBootPerformanceMetricsRequest
		return DeviceBootPerformanceMetricsRequest(self.request_adapter, self.path_parameters)

	@property
	def reboot_analytics_metrics(self,
	) -> RebootAnalyticsMetricsRequest:
		from .reboot_analytics_metrics import RebootAnalyticsMetricsRequest
		return RebootAnalyticsMetricsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_performance_metrics(self,
	) -> ResourcePerformanceMetricsRequest:
		from .resource_performance_metrics import ResourcePerformanceMetricsRequest
		return ResourcePerformanceMetricsRequest(self.request_adapter, self.path_parameters)

	@property
	def work_from_anywhere_metrics(self,
	) -> WorkFromAnywhereMetricsRequest:
		from .work_from_anywhere_metrics import WorkFromAnywhereMetricsRequest
		return WorkFromAnywhereMetricsRequest(self.request_adapter, self.path_parameters)

