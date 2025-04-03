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
	from .industry_data_start import IndustryDataStartRequest
	from .industry_data_get_statistics import IndustryDataGetStatisticsRequest
	from .count import CountRequest
	from .by_industry_data_run_id import ByIndustryDataRunIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.industry_data_industry_data_run_collection_response import IndustryDataIndustryDataRunCollectionResponse


class RunsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/industryData/runs", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IndustryDataIndustryDataRunCollectionResponse:
		"""
		List industryDataRuns
		Get a list of the industryDataRun objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/industrydata-industrydatarun-list?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, IndustryDataIndustryDataRunCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> RunsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RunsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RunsRequest(self.request_adapter, self.path_parameters)

	def by_industry_data_run_id(self,
		industryDataRun_id: str,
	) -> ByIndustryDataRunIdRequest:
		if industryDataRun_id is None:
			raise TypeError("industryDataRun_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["industryDataRun%2Did"] =  industryDataRun_id

		from .by_industry_data_run_id import ByIndustryDataRunIdRequest
		return ByIndustryDataRunIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def industry_data_get_statistics(self,
	) -> IndustryDataGetStatisticsRequest:
		from .industry_data_get_statistics import IndustryDataGetStatisticsRequest
		return IndustryDataGetStatisticsRequest(self.request_adapter, self.path_parameters)

	@property
	def industry_data_start(self,
	) -> IndustryDataStartRequest:
		from .industry_data_start import IndustryDataStartRequest
		return IndustryDataStartRequest(self.request_adapter, self.path_parameters)

