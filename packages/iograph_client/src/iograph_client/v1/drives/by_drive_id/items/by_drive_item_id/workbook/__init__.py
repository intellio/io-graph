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
	from .worksheets import WorksheetsRequest
	from .tables import TablesRequest
	from .operations import OperationsRequest
	from .names import NamesRequest
	from .table_row_operation_result_with_key import TableRowOperationResultWithKeyRequest
	from .session_info_resource_with_key import SessionInfoResourceWithKeyRequest
	from .refresh_session import RefreshSessionRequest
	from .create_session import CreateSessionRequest
	from .close_session import CloseSessionRequest
	from .functions import FunctionsRequest
	from .comments import CommentsRequest
	from .application import ApplicationRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.workbook import Workbook
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


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

	def application(self,
		drive_id: str,
		driveItem_id: str,
	) -> ApplicationRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .application import ApplicationRequest
		return ApplicationRequest(self.request_adapter, path_parameters)

	def comments(self,
		drive_id: str,
		driveItem_id: str,
	) -> CommentsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .comments import CommentsRequest
		return CommentsRequest(self.request_adapter, path_parameters)

	def functions(self,
		drive_id: str,
		driveItem_id: str,
	) -> FunctionsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .functions import FunctionsRequest
		return FunctionsRequest(self.request_adapter, path_parameters)

	def close_session(self,
		drive_id: str,
		driveItem_id: str,
	) -> CloseSessionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .close_session import CloseSessionRequest
		return CloseSessionRequest(self.request_adapter, path_parameters)

	def create_session(self,
		drive_id: str,
		driveItem_id: str,
	) -> CreateSessionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .create_session import CreateSessionRequest
		return CreateSessionRequest(self.request_adapter, path_parameters)

	def refresh_session(self,
		drive_id: str,
		driveItem_id: str,
	) -> RefreshSessionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .refresh_session import RefreshSessionRequest
		return RefreshSessionRequest(self.request_adapter, path_parameters)

	def session_info_resource_with_key(self,
		drive_id: str,
		driveItem_id: str,
		key: str,
	) -> SessionInfoResourceWithKeyRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if key is None:
			raise TypeError("key cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["key"] =  key

		from .session_info_resource_with_key import SessionInfoResourceWithKeyRequest
		return SessionInfoResourceWithKeyRequest(self.request_adapter, path_parameters)

	def table_row_operation_result_with_key(self,
		drive_id: str,
		driveItem_id: str,
		key: str,
	) -> TableRowOperationResultWithKeyRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if key is None:
			raise TypeError("key cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["key"] =  key

		from .table_row_operation_result_with_key import TableRowOperationResultWithKeyRequest
		return TableRowOperationResultWithKeyRequest(self.request_adapter, path_parameters)

	def names(self,
		drive_id: str,
		driveItem_id: str,
	) -> NamesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .names import NamesRequest
		return NamesRequest(self.request_adapter, path_parameters)

	def operations(self,
		drive_id: str,
		driveItem_id: str,
	) -> OperationsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .operations import OperationsRequest
		return OperationsRequest(self.request_adapter, path_parameters)

	def tables(self,
		drive_id: str,
		driveItem_id: str,
	) -> TablesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .tables import TablesRequest
		return TablesRequest(self.request_adapter, path_parameters)

	def worksheets(self,
		drive_id: str,
		driveItem_id: str,
	) -> WorksheetsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id

		from .worksheets import WorksheetsRequest
		return WorksheetsRequest(self.request_adapter, path_parameters)

