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
	from .by_mac_o_s_software_update_category_summary_id import ByMacOSSoftwareUpdateCategorySummaryIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.mac_o_s_software_update_category_summary import MacOSSoftwareUpdateCategorySummary
from iograph_models.beta.mac_o_s_software_update_category_summary_collection_response import MacOSSoftwareUpdateCategorySummaryCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class CategorySummariesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/macOSSoftwareUpdateAccountSummaries/{macOSSoftwareUpdateAccountSummary%2Did}/categorySummaries", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MacOSSoftwareUpdateCategorySummaryCollectionResponse:
		"""
		Get categorySummaries from deviceManagement
		Summary of the updates by category.
		"""
		tags = ['deviceManagement.macOSSoftwareUpdateAccountSummary']

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
		return await self.request_adapter.send_async(request_info, MacOSSoftwareUpdateCategorySummaryCollectionResponse, error_mapping)

	async def post(
		self,
		body: MacOSSoftwareUpdateCategorySummary,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MacOSSoftwareUpdateCategorySummary:
		"""
		Create new navigation property to categorySummaries for deviceManagement
		
		"""
		tags = ['deviceManagement.macOSSoftwareUpdateAccountSummary']

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
		return await self.request_adapter.send_async(request_info, MacOSSoftwareUpdateCategorySummary, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> CategorySummariesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CategorySummariesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CategorySummariesRequest(self.request_adapter, self.path_parameters)

	def by_mac_o_s_software_update_category_summary_id(self,
		macOSSoftwareUpdateAccountSummary_id: str,
		macOSSoftwareUpdateCategorySummary_id: str,
	) -> ByMacOSSoftwareUpdateCategorySummaryIdRequest:
		if macOSSoftwareUpdateAccountSummary_id is None:
			raise TypeError("macOSSoftwareUpdateAccountSummary_id cannot be null.")
		if macOSSoftwareUpdateCategorySummary_id is None:
			raise TypeError("macOSSoftwareUpdateCategorySummary_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["macOSSoftwareUpdateAccountSummary%2Did"] =  macOSSoftwareUpdateAccountSummary_id
		path_parameters["macOSSoftwareUpdateCategorySummary%2Did"] =  macOSSoftwareUpdateCategorySummary_id

		from .by_mac_o_s_software_update_category_summary_id import ByMacOSSoftwareUpdateCategorySummaryIdRequest
		return ByMacOSSoftwareUpdateCategorySummaryIdRequest(self.request_adapter, path_parameters)

	def count(self,
		macOSSoftwareUpdateAccountSummary_id: str,
	) -> CountRequest:
		if macOSSoftwareUpdateAccountSummary_id is None:
			raise TypeError("macOSSoftwareUpdateAccountSummary_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["macOSSoftwareUpdateAccountSummary%2Did"] =  macOSSoftwareUpdateAccountSummary_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

