# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tasks import TasksRequest
	from .start import StartRequest
	from .redirect import RedirectRequest
	from .cancel import CancelRequest
	from .abort import AbortRequest
	from .documents import DocumentsRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.print_job import PrintJob
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrintJobIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/print/printers/{printer%2Did}/jobs/{printJob%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintJob:
		"""
		Get printJob
		Retrieve the properties and relationships of a print job.
		Find more info here: https://learn.microsoft.com/graph/api/printjob-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, PrintJob, error_mapping)

	async def patch(
		self,
		body: PrintJob,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintJob:
		"""
		Update printJob
		Update a print job. Only the configuration property can be updated. Updating a print job will only succeed if there is a printTask in a processing state on the associated print job, started by a trigger that the requesting app created. For details about how to register a task trigger, see Extending Universal Print to support pull printing.
		Find more info here: https://learn.microsoft.com/graph/api/printjob-update?view=graph-rest-1.0
		"""
		tags = ['print.printer']

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
		tags = ['print.printer']
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



	@property
	def documents(self,
	) -> DocumentsRequest:
		from .documents import DocumentsRequest
		return DocumentsRequest(self.request_adapter, self.path_parameters)

	@property
	def abort(self,
	) -> AbortRequest:
		from .abort import AbortRequest
		return AbortRequest(self.request_adapter, self.path_parameters)

	@property
	def cancel(self,
	) -> CancelRequest:
		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, self.path_parameters)

	@property
	def redirect(self,
	) -> RedirectRequest:
		from .redirect import RedirectRequest
		return RedirectRequest(self.request_adapter, self.path_parameters)

	@property
	def start(self,
	) -> StartRequest:
		from .start import StartRequest
		return StartRequest(self.request_adapter, self.path_parameters)

	@property
	def tasks(self,
	) -> TasksRequest:
		from .tasks import TasksRequest
		return TasksRequest(self.request_adapter, self.path_parameters)

