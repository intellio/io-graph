# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.security_aggregated_apps_details_with_period_get_response import Security_aggregated_apps_details_with_periodGetResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SecurityAggregatedAppsDetailsWithPeriodRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/security/dataDiscovery/cloudAppDiscovery/uploadedStreams/{cloudAppDiscoveryReport%2Did}/microsoft.graph.security.aggregatedAppsDetails(period={period})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Security_aggregated_apps_details_with_periodGetResponse:
		"""
		Invoke function aggregatedAppsDetails
		
		"""
		tags = ['security.dataDiscoveryRoot']

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
		return await self.request_adapter.send_async(request_info, Security_aggregated_apps_details_with_periodGetResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> SecurityAggregatedAppsDetailsWithPeriodRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SecurityAggregatedAppsDetailsWithPeriodRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SecurityAggregatedAppsDetailsWithPeriodRequest(self.request_adapter, self.path_parameters)

