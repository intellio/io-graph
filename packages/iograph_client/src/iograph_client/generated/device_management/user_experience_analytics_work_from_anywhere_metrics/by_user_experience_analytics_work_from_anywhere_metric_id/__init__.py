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
	from .metric_devices import MetricDevicesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserExperienceAnalyticsWorkFromAnywhereMetricIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsWorkFromAnywhereMetrics/{userExperienceAnalyticsWorkFromAnywhereMetric%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsWorkFromAnywhereMetric:
		"""
		Get userExperienceAnalyticsWorkFromAnywhereMetrics from deviceManagement
		User experience analytics work from anywhere metrics.
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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsWorkFromAnywhereMetric, error_mapping)

	async def patch(
		self,
		body: UserExperienceAnalyticsWorkFromAnywhereMetric,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsWorkFromAnywhereMetric:
		"""
		Update the navigation property userExperienceAnalyticsWorkFromAnywhereMetrics in deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsWorkFromAnywhereMetric']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsWorkFromAnywhereMetric, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property userExperienceAnalyticsWorkFromAnywhereMetrics for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsWorkFromAnywhereMetric']
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



	def with_url(self, raw_url: str) -> ByUserExperienceAnalyticsWorkFromAnywhereMetricIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserExperienceAnalyticsWorkFromAnywhereMetricIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserExperienceAnalyticsWorkFromAnywhereMetricIdRequest(self.request_adapter, self.path_parameters)

	def metric_devices(self,
		userExperienceAnalyticsWorkFromAnywhereMetric_id: str,
	) -> MetricDevicesRequest:
		if userExperienceAnalyticsWorkFromAnywhereMetric_id is None:
			raise TypeError("userExperienceAnalyticsWorkFromAnywhereMetric_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsWorkFromAnywhereMetric%2Did"] =  userExperienceAnalyticsWorkFromAnywhereMetric_id

		from .metric_devices import MetricDevicesRequest
		return MetricDevicesRequest(self.request_adapter, path_parameters)

