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
	from .by_print_job_id import ByPrintJobIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.print_job_collection_response import PrintJobCollectionResponse
from iograph_models.v1.print_job import PrintJob
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class JobsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/shares/{printerShare%2Did}/jobs", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintJobCollectionResponse:
		"""
		List printJobs for a printerShare
		Retrieve a list of print jobs associated with the printerShare.
		Find more info here: https://learn.microsoft.com/graph/api/printershare-list-jobs?view=graph-rest-1.0
		"""
		tags = ['print.printerShare']

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
		return await self.request_adapter.send_async(request_info, PrintJobCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrintJob,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintJob:
		"""
		Create printJob for a printerShare
		Create a new printJob for a printerShare.  Also creates a new printDocument associated with the printJob.
		Find more info here: https://learn.microsoft.com/graph/api/printershare-post-jobs?view=graph-rest-1.0
		"""
		tags = ['print.printerShare']

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
		return await self.request_adapter.send_async(request_info, PrintJob, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> JobsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: JobsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return JobsRequest(self.request_adapter, self.path_parameters)

	def by_print_job_id(self,
		printerShare_id: str,
		printJob_id: str,
	) -> ByPrintJobIdRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .by_print_job_id import ByPrintJobIdRequest
		return ByPrintJobIdRequest(self.request_adapter, path_parameters)

	def count(self,
		printerShare_id: str,
	) -> CountRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

