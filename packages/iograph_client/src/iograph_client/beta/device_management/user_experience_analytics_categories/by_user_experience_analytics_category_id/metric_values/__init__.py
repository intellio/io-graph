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
	from .by_user_experience_analytics_metric_id import ByUserExperienceAnalyticsMetricIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.user_experience_analytics_metric import UserExperienceAnalyticsMetric
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.user_experience_analytics_metric_collection_response import UserExperienceAnalyticsMetricCollectionResponse


class MetricValuesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsCategories/{userExperienceAnalyticsCategory%2Did}/metricValues", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> UserExperienceAnalyticsMetricCollectionResponse:
		"""
		Get metricValues from deviceManagement
		The metric values for the user experience analytics category. Read-only.
		"""
		tags = ['deviceManagement.userExperienceAnalyticsCategory']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsMetricCollectionResponse, error_mapping)

	async def post(
		self,
		body: UserExperienceAnalyticsMetric,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserExperienceAnalyticsMetric:
		"""
		Create new navigation property to metricValues for deviceManagement
		
		"""
		tags = ['deviceManagement.userExperienceAnalyticsCategory']

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
		return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsMetric, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MetricValuesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MetricValuesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MetricValuesRequest(self.request_adapter, self.path_parameters)

	def by_user_experience_analytics_metric_id(self,
		userExperienceAnalyticsCategory_id: str,
		userExperienceAnalyticsMetric_id: str,
	) -> ByUserExperienceAnalyticsMetricIdRequest:
		if userExperienceAnalyticsCategory_id is None:
			raise TypeError("userExperienceAnalyticsCategory_id cannot be null.")
		if userExperienceAnalyticsMetric_id is None:
			raise TypeError("userExperienceAnalyticsMetric_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsCategory%2Did"] =  userExperienceAnalyticsCategory_id
		path_parameters["userExperienceAnalyticsMetric%2Did"] =  userExperienceAnalyticsMetric_id

		from .by_user_experience_analytics_metric_id import ByUserExperienceAnalyticsMetricIdRequest
		return ByUserExperienceAnalyticsMetricIdRequest(self.request_adapter, path_parameters)

	def count(self,
		userExperienceAnalyticsCategory_id: str,
	) -> CountRequest:
		if userExperienceAnalyticsCategory_id is None:
			raise TypeError("userExperienceAnalyticsCategory_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["userExperienceAnalyticsCategory%2Did"] =  userExperienceAnalyticsCategory_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

