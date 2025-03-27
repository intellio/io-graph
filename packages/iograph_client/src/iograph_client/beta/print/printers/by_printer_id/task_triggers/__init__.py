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
	from .by_print_task_trigger_id import ByPrintTaskTriggerIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.print_task_trigger import PrintTaskTrigger
from iograph_models.beta.print_task_trigger_collection_response import PrintTaskTriggerCollectionResponse


class TaskTriggersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/printers/{printer%2Did}/taskTriggers", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintTaskTriggerCollectionResponse:
		"""
		List taskTriggers
		Retrieve a list of task triggers associated with the printer. The list of task triggers defines which tasks will be triggered as a result of events that occur during printing. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
		Find more info here: https://learn.microsoft.com/graph/api/printer-list-tasktriggers?view=graph-rest-beta
		"""
		tags = ['print.printer']

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
		return await self.request_adapter.send_async(request_info, PrintTaskTriggerCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrintTaskTrigger,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintTaskTrigger:
		"""
		Create taskTrigger
		Create a new task trigger on the specified printer. Currently, only one task trigger can be specified per printer, but this limit might be removed in the future. 
		Find more info here: https://learn.microsoft.com/graph/api/printer-post-tasktriggers?view=graph-rest-beta
		"""
		tags = ['print.printer']

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
		return await self.request_adapter.send_async(request_info, PrintTaskTrigger, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> TaskTriggersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: TaskTriggersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return TaskTriggersRequest(self.request_adapter, self.path_parameters)

	def by_print_task_trigger_id(self,
		printer_id: str,
		printTaskTrigger_id: str,
	) -> ByPrintTaskTriggerIdRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")
		if printTaskTrigger_id is None:
			raise TypeError("printTaskTrigger_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id
		path_parameters["printTaskTrigger%2Did"] =  printTaskTrigger_id

		from .by_print_task_trigger_id import ByPrintTaskTriggerIdRequest
		return ByPrintTaskTriggerIdRequest(self.request_adapter, path_parameters)

	def count(self,
		printer_id: str,
	) -> CountRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

