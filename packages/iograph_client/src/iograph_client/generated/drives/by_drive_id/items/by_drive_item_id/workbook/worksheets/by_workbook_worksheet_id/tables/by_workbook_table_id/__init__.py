# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .worksheet import WorksheetRequest
	from .sort import SortRequest
	from .rows import RowsRequest
	from .reapply_filters import ReapplyFiltersRequest
	from .convert_to_range import ConvertToRangeRequest
	from .clear_filters import ClearFiltersRequest
	from .columns import ColumnsRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_table import WorkbookTable
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByWorkbookTableIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/tables/{workbookTable%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookTable:
		"""
		Get tables from drives
		The list of tables that are part of the worksheet. Read-only.
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
		return await self.request_adapter.send_async(request_info, WorkbookTable, error_mapping)

	async def patch(
		self,
		body: WorkbookTable,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookTable:
		"""
		Update the navigation property tables in drives
		
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
		return await self.request_adapter.send_async(request_info, WorkbookTable, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property tables for drives
		
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



	@property
	def columns(self,
	) -> ColumnsRequest:
		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, self.path_parameters)

	@property
	def clear_filters(self,
	) -> ClearFiltersRequest:
		from .clear_filters import ClearFiltersRequest
		return ClearFiltersRequest(self.request_adapter, self.path_parameters)

	@property
	def convert_to_range(self,
	) -> ConvertToRangeRequest:
		from .convert_to_range import ConvertToRangeRequest
		return ConvertToRangeRequest(self.request_adapter, self.path_parameters)

	@property
	def reapply_filters(self,
	) -> ReapplyFiltersRequest:
		from .reapply_filters import ReapplyFiltersRequest
		return ReapplyFiltersRequest(self.request_adapter, self.path_parameters)

	@property
	def rows(self,
	) -> RowsRequest:
		from .rows import RowsRequest
		return RowsRequest(self.request_adapter, self.path_parameters)

	@property
	def sort(self,
	) -> SortRequest:
		from .sort import SortRequest
		return SortRequest(self.request_adapter, self.path_parameters)

	@property
	def worksheet(self,
	) -> WorksheetRequest:
		from .worksheet import WorksheetRequest
		return WorksheetRequest(self.request_adapter, self.path_parameters)

