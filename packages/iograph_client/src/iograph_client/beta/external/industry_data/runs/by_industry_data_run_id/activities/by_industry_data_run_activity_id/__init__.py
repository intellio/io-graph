# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .activity import ActivityRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.industry_data_industry_data_run_activity import IndustryDataIndustryDataRunActivity


class ByIndustryDataRunActivityIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/external/industryData/runs/{industryDataRun%2Did}/activities/{industryDataRunActivity%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> IndustryDataIndustryDataRunActivity:
		"""
		Get activities from external
		The set of activities performed during the run.
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
		return await self.request_adapter.send_async(request_info, IndustryDataIndustryDataRunActivity, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ByIndustryDataRunActivityIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByIndustryDataRunActivityIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByIndustryDataRunActivityIdRequest(self.request_adapter, self.path_parameters)

	def activity(self,
		industryDataRun_id: str,
		industryDataRunActivity_id: str,
	) -> ActivityRequest:
		if industryDataRun_id is None:
			raise TypeError("industryDataRun_id cannot be null.")
		if industryDataRunActivity_id is None:
			raise TypeError("industryDataRunActivity_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["industryDataRun%2Did"] =  industryDataRun_id
		path_parameters["industryDataRunActivity%2Did"] =  industryDataRunActivity_id

		from .activity import ActivityRequest
		return ActivityRequest(self.request_adapter, path_parameters)

