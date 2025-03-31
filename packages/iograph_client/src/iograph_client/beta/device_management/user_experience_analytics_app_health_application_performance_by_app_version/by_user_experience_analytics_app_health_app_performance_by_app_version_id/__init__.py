# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.user_experience_analytics_app_health_app_performance_by_app_version import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion/{userExperienceAnalyticsAppHealthAppPerformanceByAppVersion%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion:
		"""
		Get userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion from deviceManagement
		User experience analytics appHealth Application Performance by App Version
		"""
		tags = ['deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByAppVersion']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion, error_mapping)

	async def patch(
		self,
		body: UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion:
		"""
		Update the navigation property userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion in deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByAppVersion']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsAppHealthAppPerformanceByAppVersion, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersion for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsAppHealthAppPerformanceByAppVersion']
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



	def with_url(self, raw_url: str) -> ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByUserExperienceAnalyticsAppHealthAppPerformanceByAppVersionIdRequest(self.request_adapter, self.path_parameters)

