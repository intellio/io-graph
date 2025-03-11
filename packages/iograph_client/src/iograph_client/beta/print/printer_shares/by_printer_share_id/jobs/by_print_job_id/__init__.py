# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tasks import TasksRequest
	from .start_print_job import StartPrintJobRequest
	from .start import StartRequest
	from .redirect import RedirectRequest
	from .cancel_print_job import CancelPrintJobRequest
	from .cancel import CancelRequest
	from .abort import AbortRequest
	from .documents import DocumentsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.print_job import PrintJob
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrintJobIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/printerShares/{printerShare%2Did}/jobs/{printJob%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintJob:
		"""
		Get jobs from print
		The list of jobs that are queued for printing by the printer/printerShare.
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
		return await self.request_adapter.send_async(request_info, PrintJob, error_mapping)

	async def patch(
		self,
		body: PrintJob,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintJob:
		"""
		Update the navigation property jobs in print
		
		"""
		tags = ['print.printerShare']

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
		return await self.request_adapter.send_async(request_info, PrintJob, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property jobs for print
		
		"""
		tags = ['print.printerShare']
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



	def with_url(self, raw_url: str) -> ByPrintJobIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrintJobIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrintJobIdRequest(self.request_adapter, self.path_parameters)

	def documents(self,
		printerShare_id: str,
		printJob_id: str,
	) -> DocumentsRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .documents import DocumentsRequest
		return DocumentsRequest(self.request_adapter, path_parameters)

	def abort(self,
		printerShare_id: str,
		printJob_id: str,
	) -> AbortRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .abort import AbortRequest
		return AbortRequest(self.request_adapter, path_parameters)

	def cancel(self,
		printerShare_id: str,
		printJob_id: str,
	) -> CancelRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def cancel_print_job(self,
		printerShare_id: str,
		printJob_id: str,
	) -> CancelPrintJobRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .cancel_print_job import CancelPrintJobRequest
		return CancelPrintJobRequest(self.request_adapter, path_parameters)

	def redirect(self,
		printerShare_id: str,
		printJob_id: str,
	) -> RedirectRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .redirect import RedirectRequest
		return RedirectRequest(self.request_adapter, path_parameters)

	def start(self,
		printerShare_id: str,
		printJob_id: str,
	) -> StartRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .start import StartRequest
		return StartRequest(self.request_adapter, path_parameters)

	def start_print_job(self,
		printerShare_id: str,
		printJob_id: str,
	) -> StartPrintJobRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .start_print_job import StartPrintJobRequest
		return StartPrintJobRequest(self.request_adapter, path_parameters)

	def tasks(self,
		printerShare_id: str,
		printJob_id: str,
	) -> TasksRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, path_parameters)

