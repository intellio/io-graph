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
	from .count import CountRequest
	from .by_print_task_id import ByPrintTaskIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.print_task import PrintTask
from iograph_models.v1.print_task_collection_response import PrintTaskCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class TasksRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/shares/{printerShare%2Did}/jobs/{printJob%2Did}/tasks", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintTaskCollectionResponse:
		"""
		Get tasks from print
		A list of printTasks that were triggered by this print job.
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
		return await self.request_adapter.send_async(request_info, PrintTaskCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrintTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintTask:
		"""
		Create new navigation property to tasks for print
		
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
		return await self.request_adapter.send_async(request_info, PrintTask, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TasksRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TasksRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TasksRequest(self.request_adapter, self.path_parameters)

	def by_print_task_id(self,
		printerShare_id: str,
		printJob_id: str,
		printTask_id: str,
	) -> ByPrintTaskIdRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")
		if printTask_id is None:
			raise TypeError("printTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id
		path_parameters["printTask%2Did"] =  printTask_id

		from .by_print_task_id import ByPrintTaskIdRequest
		return ByPrintTaskIdRequest(self.request_adapter, path_parameters)

	def count(self,
		printerShare_id: str,
		printJob_id: str,
	) -> CountRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

