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
	from .trigger import TriggerRequest
	from .definition import DefinitionRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.print_task import PrintTask


class ByPrintTaskIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/taskDefinitions/{printTaskDefinition%2Did}/tasks/{printTask%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintTask:
		"""
		Get task
		Get details about a print task. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
		Find more info here: https://learn.microsoft.com/graph/api/printtask-get?view=graph-rest-beta
		"""
		tags = ['print.printTaskDefinition']

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
		return await self.request_adapter.send_async(request_info, PrintTask, error_mapping)

	async def patch(
		self,
		body: PrintTask,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintTask:
		"""
		Update task
		Update a print task. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
		Find more info here: https://learn.microsoft.com/graph/api/printtaskdefinition-update-task?view=graph-rest-beta
		"""
		tags = ['print.printTaskDefinition']

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
		return await self.request_adapter.send_async(request_info, PrintTask, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property tasks for print
		
		"""
		tags = ['print.printTaskDefinition']
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



	def with_url(self, raw_url: str) -> ByPrintTaskIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrintTaskIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrintTaskIdRequest(self.request_adapter, self.path_parameters)

	def definition(self,
		printTaskDefinition_id: str,
		printTask_id: str,
	) -> DefinitionRequest:
		if printTaskDefinition_id is None:
			raise TypeError("printTaskDefinition_id cannot be null.")
		if printTask_id is None:
			raise TypeError("printTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printTaskDefinition%2Did"] =  printTaskDefinition_id
		path_parameters["printTask%2Did"] =  printTask_id

		from .definition import DefinitionRequest
		return DefinitionRequest(self.request_adapter, path_parameters)

	def trigger(self,
		printTaskDefinition_id: str,
		printTask_id: str,
	) -> TriggerRequest:
		if printTaskDefinition_id is None:
			raise TypeError("printTaskDefinition_id cannot be null.")
		if printTask_id is None:
			raise TypeError("printTask_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printTaskDefinition%2Did"] =  printTaskDefinition_id
		path_parameters["printTask%2Did"] =  printTask_id

		from .trigger import TriggerRequest
		return TriggerRequest(self.request_adapter, path_parameters)

