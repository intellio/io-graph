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
	from .worksheet import WorksheetRequest
	from .sort import SortRequest
	from .rows import RowsRequest
	from .total_row_range import TotalRowRangeRequest
	from .reapply_filters import ReapplyFiltersRequest
	from .range import RangeRequest
	from .header_row_range import HeaderRowRangeRequest
	from .data_body_range import DataBodyRangeRequest
	from .convert_to_range import ConvertToRangeRequest
	from .clear_filters import ClearFiltersRequest
	from .columns import ColumnsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_table import WorkbookTable
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByWorkbookTableIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tables/{workbookTable%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookTable:
		"""
		Get tables from drives
		Represents a collection of tables associated with the workbook. Read-only.
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



	def with_url(self, raw_url: str) -> ByWorkbookTableIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWorkbookTableIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWorkbookTableIdRequest(self.request_adapter, self.path_parameters)

	def columns(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> ColumnsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, path_parameters)

	def clear_filters(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> ClearFiltersRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .clear_filters import ClearFiltersRequest
		return ClearFiltersRequest(self.request_adapter, path_parameters)

	def convert_to_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> ConvertToRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .convert_to_range import ConvertToRangeRequest
		return ConvertToRangeRequest(self.request_adapter, path_parameters)

	def data_body_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> DataBodyRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .data_body_range import DataBodyRangeRequest
		return DataBodyRangeRequest(self.request_adapter, path_parameters)

	def header_row_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> HeaderRowRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .header_row_range import HeaderRowRangeRequest
		return HeaderRowRangeRequest(self.request_adapter, path_parameters)

	def range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> RangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .range import RangeRequest
		return RangeRequest(self.request_adapter, path_parameters)

	def reapply_filters(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> ReapplyFiltersRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .reapply_filters import ReapplyFiltersRequest
		return ReapplyFiltersRequest(self.request_adapter, path_parameters)

	def total_row_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> TotalRowRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .total_row_range import TotalRowRangeRequest
		return TotalRowRangeRequest(self.request_adapter, path_parameters)

	def rows(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> RowsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .rows import RowsRequest
		return RowsRequest(self.request_adapter, path_parameters)

	def sort(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> SortRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .sort import SortRequest
		return SortRequest(self.request_adapter, path_parameters)

	def worksheet(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
	) -> WorksheetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .worksheet import WorksheetRequest
		return WorksheetRequest(self.request_adapter, path_parameters)

