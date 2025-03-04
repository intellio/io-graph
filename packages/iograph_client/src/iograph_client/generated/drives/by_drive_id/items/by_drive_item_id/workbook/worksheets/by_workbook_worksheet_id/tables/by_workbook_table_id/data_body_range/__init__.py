# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .worksheet import WorksheetRequest
	from .sort import SortRequest
	from .visible_view import VisibleViewRequest
	from .used_range import UsedRangeRequest
	from .unmerge import UnmergeRequest
	from .rows_below import RowsBelowRequest
	from .rows_above import RowsAboveRequest
	from .row import RowRequest
	from .resized_range import ResizedRangeRequest
	from .offset_range import OffsetRangeRequest
	from .merge import MergeRequest
	from .last_row import LastRowRequest
	from .last_column import LastColumnRequest
	from .last_cell import LastCellRequest
	from .intersection import IntersectionRequest
	from .insert import InsertRequest
	from .entire_row import EntireRowRequest
	from .entire_column import EntireColumnRequest
	from .delete import DeleteRequest
	from .columns_before import ColumnsBeforeRequest
	from .columns_after import ColumnsAfterRequest
	from .column import ColumnRequest
	from .clear import ClearRequest
	from .cell import CellRequest
	from .bounding_rect import BoundingRectRequest
	from .format import FormatRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.workbook_range import WorkbookRange


class DataBodyRangeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/tables/{workbookTable%2Did}/dataBodyRange()", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookRange:
		"""
		Invoke function dataBodyRange
		Gets the range object associated with the data body of the table.
		Find more info here: https://learn.microsoft.com/graph/api/table-databodyrange?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, WorkbookRange, error_mapping)


	def with_url(self, raw_url: str) -> DataBodyRangeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DataBodyRangeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DataBodyRangeRequest(self.request_adapter, self.path_parameters)

	def format(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> FormatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .format import FormatRequest
		return FormatRequest(self.request_adapter, path_parameters)

	def bounding_rect(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		anotherRange: str,
	) -> BoundingRectRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if anotherRange is None:
			raise TypeError("anotherRange cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["anotherRange"] =  anotherRange

		from .bounding_rect import BoundingRectRequest
		return BoundingRectRequest(self.request_adapter, path_parameters)

	def cell(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		row: int,
		column: int,
	) -> CellRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .cell import CellRequest
		return CellRequest(self.request_adapter, path_parameters)

	def clear(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> ClearRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .clear import ClearRequest
		return ClearRequest(self.request_adapter, path_parameters)

	def column(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		column: int,
	) -> ColumnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["column"] =  column

		from .column import ColumnRequest
		return ColumnRequest(self.request_adapter, path_parameters)

	def columns_after(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> ColumnsAfterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .columns_after import ColumnsAfterRequest
		return ColumnsAfterRequest(self.request_adapter, path_parameters)

	def columns_before(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> ColumnsBeforeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .columns_before import ColumnsBeforeRequest
		return ColumnsBeforeRequest(self.request_adapter, path_parameters)

	def delete(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> DeleteRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .delete import DeleteRequest
		return DeleteRequest(self.request_adapter, path_parameters)

	def entire_column(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> EntireColumnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .entire_column import EntireColumnRequest
		return EntireColumnRequest(self.request_adapter, path_parameters)

	def entire_row(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> EntireRowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .entire_row import EntireRowRequest
		return EntireRowRequest(self.request_adapter, path_parameters)

	def insert(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> InsertRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .insert import InsertRequest
		return InsertRequest(self.request_adapter, path_parameters)

	def intersection(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		anotherRange: str,
	) -> IntersectionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if anotherRange is None:
			raise TypeError("anotherRange cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["anotherRange"] =  anotherRange

		from .intersection import IntersectionRequest
		return IntersectionRequest(self.request_adapter, path_parameters)

	def last_cell(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> LastCellRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .last_cell import LastCellRequest
		return LastCellRequest(self.request_adapter, path_parameters)

	def last_column(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> LastColumnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .last_column import LastColumnRequest
		return LastColumnRequest(self.request_adapter, path_parameters)

	def last_row(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> LastRowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .last_row import LastRowRequest
		return LastRowRequest(self.request_adapter, path_parameters)

	def merge(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> MergeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .merge import MergeRequest
		return MergeRequest(self.request_adapter, path_parameters)

	def offset_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		rowOffset: int,
		columnOffset: int,
	) -> OffsetRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if rowOffset is None:
			raise TypeError("rowOffset cannot be null.")
		if columnOffset is None:
			raise TypeError("columnOffset cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["rowOffset"] =  rowOffset
		path_parameters["columnOffset"] =  columnOffset

		from .offset_range import OffsetRangeRequest
		return OffsetRangeRequest(self.request_adapter, path_parameters)

	def resized_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		deltaRows: int,
		deltaColumns: int,
	) -> ResizedRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if deltaRows is None:
			raise TypeError("deltaRows cannot be null.")
		if deltaColumns is None:
			raise TypeError("deltaColumns cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["deltaRows"] =  deltaRows
		path_parameters["deltaColumns"] =  deltaColumns

		from .resized_range import ResizedRangeRequest
		return ResizedRangeRequest(self.request_adapter, path_parameters)

	def row(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		row: int,
	) -> RowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["row"] =  row

		from .row import RowRequest
		return RowRequest(self.request_adapter, path_parameters)

	def rows_above(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> RowsAboveRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .rows_above import RowsAboveRequest
		return RowsAboveRequest(self.request_adapter, path_parameters)

	def rows_below(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> RowsBelowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .rows_below import RowsBelowRequest
		return RowsBelowRequest(self.request_adapter, path_parameters)

	def unmerge(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> UnmergeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .unmerge import UnmergeRequest
		return UnmergeRequest(self.request_adapter, path_parameters)

	def used_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> UsedRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .used_range import UsedRangeRequest
		return UsedRangeRequest(self.request_adapter, path_parameters)

	def visible_view(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> VisibleViewRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .visible_view import VisibleViewRequest
		return VisibleViewRequest(self.request_adapter, path_parameters)

	def sort(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> SortRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .sort import SortRequest
		return SortRequest(self.request_adapter, path_parameters)

	def worksheet(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
	) -> WorksheetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id

		from .worksheet import WorksheetRequest
		return WorksheetRequest(self.request_adapter, path_parameters)

