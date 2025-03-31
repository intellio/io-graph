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
	from .by_print_document_id import ByPrintDocumentIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.print_document_collection_response import PrintDocumentCollectionResponse
from iograph_models.v1.print_document import PrintDocument
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class DocumentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/printers/{printer%2Did}/jobs/{printJob%2Did}/documents", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintDocumentCollectionResponse:
		"""
		Download printDocument binary file
		Download the binary file associated with a printDocument. Calling this method yields a redirect response with a preauthenticated URL that can be used to download the payload.
		Find more info here: https://learn.microsoft.com/graph/api/printdocument-get-file?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, PrintDocumentCollectionResponse, error_mapping)

	async def post(
		self,
		body: PrintDocument,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintDocument:
		"""
		Create new navigation property to documents for print
		
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
		return await self.request_adapter.send_async(request_info, PrintDocument, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DocumentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DocumentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DocumentsRequest(self.request_adapter, self.path_parameters)

	def by_print_document_id(self,
		printer_id: str,
		printJob_id: str,
		printDocument_id: str,
	) -> ByPrintDocumentIdRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")
		if printDocument_id is None:
			raise TypeError("printDocument_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id
		path_parameters["printJob%2Did"] =  printJob_id
		path_parameters["printDocument%2Did"] =  printDocument_id

		from .by_print_document_id import ByPrintDocumentIdRequest
		return ByPrintDocumentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		printer_id: str,
		printJob_id: str,
	) -> CountRequest:
		if printer_id is None:
			raise TypeError("printer_id cannot be null.")
		if printJob_id is None:
			raise TypeError("printJob_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["printer%2Did"] =  printer_id
		path_parameters["printJob%2Did"] =  printJob_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

