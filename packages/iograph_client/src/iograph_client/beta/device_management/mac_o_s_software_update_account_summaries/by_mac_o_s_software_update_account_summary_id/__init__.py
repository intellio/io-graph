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
	from .category_summaries import CategorySummariesRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.mac_o_s_software_update_account_summary import MacOSSoftwareUpdateAccountSummary
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMacOSSoftwareUpdateAccountSummaryIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/macOSSoftwareUpdateAccountSummaries/{macOSSoftwareUpdateAccountSummary%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MacOSSoftwareUpdateAccountSummary:
		"""
		Get macOSSoftwareUpdateAccountSummaries from deviceManagement
		The MacOS software update account summaries for this account.
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
		return await self.request_adapter.send_async(request_info, MacOSSoftwareUpdateAccountSummary, error_mapping)

	async def patch(
		self,
		body: MacOSSoftwareUpdateAccountSummary,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MacOSSoftwareUpdateAccountSummary:
		"""
		Update the navigation property macOSSoftwareUpdateAccountSummaries in deviceManagement
		
		"""
		tags = ['deviceManagement.macOSSoftwareUpdateAccountSummary']

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
		return await self.request_adapter.send_async(request_info, MacOSSoftwareUpdateAccountSummary, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property macOSSoftwareUpdateAccountSummaries for deviceManagement
		
		"""
		tags = ['deviceManagement.macOSSoftwareUpdateAccountSummary']
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



	def with_url(self, raw_url: str) -> ByMacOSSoftwareUpdateAccountSummaryIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMacOSSoftwareUpdateAccountSummaryIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMacOSSoftwareUpdateAccountSummaryIdRequest(self.request_adapter, self.path_parameters)

	def category_summaries(self,
		macOSSoftwareUpdateAccountSummary_id: str,
	) -> CategorySummariesRequest:
		if macOSSoftwareUpdateAccountSummary_id is None:
			raise TypeError("macOSSoftwareUpdateAccountSummary_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["macOSSoftwareUpdateAccountSummary%2Did"] =  macOSSoftwareUpdateAccountSummary_id

		from .category_summaries import CategorySummariesRequest
		return CategorySummariesRequest(self.request_adapter, path_parameters)

