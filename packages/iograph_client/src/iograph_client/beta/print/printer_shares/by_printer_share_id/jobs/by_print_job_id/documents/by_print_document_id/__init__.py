# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .create_upload_session import CreateUploadSessionRequest
	from .value import ValueRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.print_document import PrintDocument
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrintDocumentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/printerShares/{printerShare%2Did}/jobs/{printJob%2Did}/documents/{printDocument%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintDocument:
		"""
		Get documents from print
		
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
		return await self.request_adapter.send_async(request_info, PrintDocument, error_mapping)

	async def patch(
		self,
		body: PrintDocument,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintDocument:
		"""
		Update the navigation property documents in print
		
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
		return await self.request_adapter.send_async(request_info, PrintDocument, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property documents for print
		
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



	def with_url(self, raw_url: str) -> ByPrintDocumentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrintDocumentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrintDocumentIdRequest(self.request_adapter, self.path_parameters)

	def value(self,
		printerShare_id: str,
		printJob_id: str,
		printDocument_id: str,
	) -> ValueRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")
		if printDocument_id is None:
			raise TypeError("printDocument_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id
		path_parameters["printDocument%2Did"] =  printDocument_id

		from .value import ValueRequest
		return ValueRequest(self.request_adapter, path_parameters)

	def create_upload_session(self,
		printerShare_id: str,
		printJob_id: str,
		printDocument_id: str,
	) -> CreateUploadSessionRequest:
		if printerShare_id is None:
			raise TypeError("printerShare_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")
		if printDocument_id is None:
			raise TypeError("printDocument_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printerShare%2Did"] =  printerShare_id
		path_parameters["printJob%2Did"] =  printJob_id
		path_parameters["printDocument%2Did"] =  printDocument_id

		from .create_upload_session import CreateUploadSessionRequest
		return CreateUploadSessionRequest(self.request_adapter, path_parameters)

