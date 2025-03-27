# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .task_definitions import TaskDefinitionsRequest
	from .shares import SharesRequest
	from .services import ServicesRequest
	from .printers import PrintersRequest
	from .operations import OperationsRequest
	from .connectors import ConnectorsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.print import Print
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class PrintRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Print:
		"""
		Get print
		
		"""
		tags = ['print.print']

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
		return await self.request_adapter.send_async(request_info, Print, error_mapping)

	async def patch(
		self,
		body: Print,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Print:
		"""
		Update print
		
		"""
		tags = ['print.print']

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
		return await self.request_adapter.send_async(request_info, Print, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PrintRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PrintRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PrintRequest(self.request_adapter, self.path_parameters)

	@property
	def connectors(self,
	) -> ConnectorsRequest:
		from .connectors import ConnectorsRequest
		return ConnectorsRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def printers(self,
	) -> PrintersRequest:
		from .printers import PrintersRequest
		return PrintersRequest(self.request_adapter, self.path_parameters)

	@property
	def services(self,
	) -> ServicesRequest:
		from .services import ServicesRequest
		return ServicesRequest(self.request_adapter, self.path_parameters)

	@property
	def shares(self,
	) -> SharesRequest:
		from .shares import SharesRequest
		return SharesRequest(self.request_adapter, self.path_parameters)

	@property
	def task_definitions(self,
	) -> TaskDefinitionsRequest:
		from .task_definitions import TaskDefinitionsRequest
		return TaskDefinitionsRequest(self.request_adapter, self.path_parameters)

