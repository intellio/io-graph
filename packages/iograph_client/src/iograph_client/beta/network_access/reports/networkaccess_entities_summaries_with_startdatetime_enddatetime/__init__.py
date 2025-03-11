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
from iograph_models.beta.networkaccess_entities_summaries_with_startdatetime_enddatetime_get_response import Networkaccess_entities_summaries_with_startdatetime_enddatetimeGetResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/reports/microsoft.graph.networkaccess.entitiesSummaries(startDateTime={startDateTime},endDateTime={endDateTime})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Networkaccess_entities_summaries_with_startdatetime_enddatetimeGetResponse:
		"""
		Invoke function entitiesSummaries
		Get the number of users, devices, and workloads per traffic type in a specified time period.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-reports-entitiessummaries?view=graph-rest-beta
		"""
		tags = ['networkAccess.reports']

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
		return await self.request_adapter.send_async(request_info, Networkaccess_entities_summaries_with_startdatetime_enddatetimeGetResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")

	def with_url(self, raw_url: str) -> NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return NetworkaccessEntitiesSummariesWithStartDateTimeEndDateTimeRequest(self.request_adapter, self.path_parameters)

