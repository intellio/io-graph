# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .worksheets import WorksheetsRequest
	from .tables import TablesRequest
	from .operations import OperationsRequest
	from .names import NamesRequest
	from .refresh_session import RefreshSessionRequest
	from .create_session import CreateSessionRequest
	from .close_session import CloseSessionRequest
	from .functions import FunctionsRequest
	from .comments import CommentsRequest
	from .application import ApplicationRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook import Workbook
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class WorkbookRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Workbook:
		"""
		Get workbook from drives
		For files that are Excel spreadsheets, access to the workbook API to work with the spreadsheet's contents. Nullable.
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, Workbook, error_mapping)

	async def patch(
		self,
		body: Workbook,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Workbook:
		"""
		Update the navigation property workbook in drives
		
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, Workbook, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property workbook for drives
		
		"""
		tags = ['drives.driveItem']
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



	def with_url(self, raw_url: str) -> WorkbookRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: WorkbookRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return WorkbookRequest(self.request_adapter, self.path_parameters)

	@property
	def application(self,
	) -> ApplicationRequest:
		from .application import ApplicationRequest
		return ApplicationRequest(self.request_adapter, self.path_parameters)

	@property
	def comments(self,
	) -> CommentsRequest:
		from .comments import CommentsRequest
		return CommentsRequest(self.request_adapter, self.path_parameters)

	@property
	def functions(self,
	) -> FunctionsRequest:
		from .functions import FunctionsRequest
		return FunctionsRequest(self.request_adapter, self.path_parameters)

	@property
	def close_session(self,
	) -> CloseSessionRequest:
		from .close_session import CloseSessionRequest
		return CloseSessionRequest(self.request_adapter, self.path_parameters)

	@property
	def create_session(self,
	) -> CreateSessionRequest:
		from .create_session import CreateSessionRequest
		return CreateSessionRequest(self.request_adapter, self.path_parameters)

	@property
	def refresh_session(self,
	) -> RefreshSessionRequest:
		from .refresh_session import RefreshSessionRequest
		return RefreshSessionRequest(self.request_adapter, self.path_parameters)

	@property
	def names(self,
	) -> NamesRequest:
		from .names import NamesRequest
		return NamesRequest(self.request_adapter, self.path_parameters)

	@property
	def operations(self,
	) -> OperationsRequest:
		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, self.path_parameters)

	@property
	def tables(self,
	) -> TablesRequest:
		from .tables import TablesRequest
		return TablesRequest(self.request_adapter, self.path_parameters)

	@property
	def worksheets(self,
	) -> WorksheetsRequest:
		from .worksheets import WorksheetsRequest
		return WorksheetsRequest(self.request_adapter, self.path_parameters)

