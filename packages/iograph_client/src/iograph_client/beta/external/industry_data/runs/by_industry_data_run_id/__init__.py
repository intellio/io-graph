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
	from .industry_data_get_statistics import IndustryDataGetStatisticsRequest
	from .activities import ActivitiesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.industry_data_industry_data_run import IndustryDataIndustryDataRun
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByIndustryDataRunIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/industryData/runs/{industryDataRun%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IndustryDataIndustryDataRun:
		"""
		Get industryDataRun
		Read the properties and relationships of an industryDataRun object.
		Find more info here: https://learn.microsoft.com/graph/api/industrydata-industrydatarun-get?view=graph-rest-beta
		"""
		tags = ['external.industryDataRoot']

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
		return await self.request_adapter.send_async(request_info, IndustryDataIndustryDataRun, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByIndustryDataRunIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByIndustryDataRunIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByIndustryDataRunIdRequest(self.request_adapter, self.path_parameters)

	def activities(self,
		industryDataRun_id: str,
	) -> ActivitiesRequest:
		if industryDataRun_id is None:
			raise TypeError("industryDataRun_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["industryDataRun%2Did"] =  industryDataRun_id

		from .activities import ActivitiesRequest
		return ActivitiesRequest(self.request_adapter, path_parameters)

	def industry_data_get_statistics(self,
		industryDataRun_id: str,
	) -> IndustryDataGetStatisticsRequest:
		if industryDataRun_id is None:
			raise TypeError("industryDataRun_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["industryDataRun%2Did"] =  industryDataRun_id

		from .industry_data_get_statistics import IndustryDataGetStatisticsRequest
		return IndustryDataGetStatisticsRequest(self.request_adapter, path_parameters)

