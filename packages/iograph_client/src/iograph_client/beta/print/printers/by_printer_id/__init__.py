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
	from .task_triggers import TaskTriggersRequest
	from .shares import SharesRequest
	from .share import ShareRequest
	from .restore_factory_defaults import RestoreFactoryDefaultsRequest
	from .reset_defaults import ResetDefaultsRequest
	from .get_capabilities import GetCapabilitiesRequest
	from .jobs import JobsRequest
	from .connectors import ConnectorsRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.printer import Printer


class ByPrinterIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/printers/{printer%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Printer:
		"""
		Get printer
		Retrieve the properties and relationships of a printer object.
		Find more info here: https://learn.microsoft.com/graph/api/printer-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, Printer, error_mapping)

	async def patch(
		self,
		body: Printer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Printer:
		"""
		Update printer
		Update the properties of a printer object.
		Find more info here: https://learn.microsoft.com/graph/api/printer-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, Printer, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete printer
		Delete (unregister) a printer.
		Find more info here: https://learn.microsoft.com/graph/api/printer-delete?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByPrinterIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrinterIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrinterIdRequest(self.request_adapter, self.path_parameters)

	def connectors(self,
		printer_id: str,
	) -> ConnectorsRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .connectors import ConnectorsRequest
		return ConnectorsRequest(self.request_adapter, path_parameters)

	def jobs(self,
		printer_id: str,
	) -> JobsRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .jobs import JobsRequest
		return JobsRequest(self.request_adapter, path_parameters)

	def get_capabilities(self,
		printer_id: str,
	) -> GetCapabilitiesRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .get_capabilities import GetCapabilitiesRequest
		return GetCapabilitiesRequest(self.request_adapter, path_parameters)

	def reset_defaults(self,
		printer_id: str,
	) -> ResetDefaultsRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .reset_defaults import ResetDefaultsRequest
		return ResetDefaultsRequest(self.request_adapter, path_parameters)

	def restore_factory_defaults(self,
		printer_id: str,
	) -> RestoreFactoryDefaultsRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .restore_factory_defaults import RestoreFactoryDefaultsRequest
		return RestoreFactoryDefaultsRequest(self.request_adapter, path_parameters)

	def share(self,
		printer_id: str,
	) -> ShareRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .share import ShareRequest
		return ShareRequest(self.request_adapter, path_parameters)

	def shares(self,
		printer_id: str,
	) -> SharesRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .shares import SharesRequest
		return SharesRequest(self.request_adapter, path_parameters)

	def task_triggers(self,
		printer_id: str,
	) -> TaskTriggersRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id

		from .task_triggers import TaskTriggersRequest
		return TaskTriggersRequest(self.request_adapter, path_parameters)

