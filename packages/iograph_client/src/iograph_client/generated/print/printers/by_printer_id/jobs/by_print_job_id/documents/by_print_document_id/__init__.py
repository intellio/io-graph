# Auto-generated client

from __future__ import annotations
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
from iograph_models.models.print_document import PrintDocument
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByPrintDocumentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/print/printers/{printer%2Did}/jobs/{printJob%2Did}/documents/{printDocument%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PrintDocument:
		"""
		Get documents from print
		
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
		return await self.request_adapter.send_async(request_info, PrintDocument, error_mapping)

	async def patch(
		self,
		body: PrintDocument,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PrintDocument:
		"""
		Update the navigation property documents in print
		
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
		return await self.request_adapter.send_async(request_info, PrintDocument, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property documents for print
		
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



	def with_url(self, raw_url: str) -> ByPrintDocumentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPrintDocumentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPrintDocumentIdRequest(self.request_adapter, self.path_parameters)

	@property
	def value(self,
	) -> ValueRequest:
		from .value import ValueRequest
		return ValueRequest(self.request_adapter, self.path_parameters)

	@property
	def create_upload_session(self,
	) -> CreateUploadSessionRequest:
		from .create_upload_session import CreateUploadSessionRequest
		return CreateUploadSessionRequest(self.request_adapter, self.path_parameters)

