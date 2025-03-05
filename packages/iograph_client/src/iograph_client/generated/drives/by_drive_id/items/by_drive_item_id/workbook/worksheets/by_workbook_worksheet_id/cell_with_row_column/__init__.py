# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .worksheet import WorksheetRequest
	from .sort import SortRequest
	from .visible_view import VisibleViewRequest
	from .used_range_with_valuesonly import UsedRangeWithValuesOnlyRequest
	from .used_range import UsedRangeRequest
	from .unmerge import UnmergeRequest
	from .rows_below_with_count import RowsBelowWithCountRequest
	from .rows_below import RowsBelowRequest
	from .rows_above_with_count import RowsAboveWithCountRequest
	from .rows_above import RowsAboveRequest
	from .row_with_row import RowWithRowRequest
	from .resized_range_with_deltarows_deltacolumns import ResizedRangeWithDeltaRowsDeltaColumnsRequest
	from .offset_range_with_rowoffset_columnoffset import OffsetRangeWithRowOffsetColumnOffsetRequest
	from .merge import MergeRequest
	from .last_row import LastRowRequest
	from .last_column import LastColumnRequest
	from .last_cell import LastCellRequest
	from .intersection_with_anotherrange import IntersectionWithAnotherRangeRequest
	from .insert import InsertRequest
	from .entire_row import EntireRowRequest
	from .entire_column import EntireColumnRequest
	from .delete import DeleteRequest
	from .columns_before_with_count import ColumnsBeforeWithCountRequest
	from .columns_before import ColumnsBeforeRequest
	from .columns_after_with_count import ColumnsAfterWithCountRequest
	from .columns_after import ColumnsAfterRequest
	from .column_with_column import ColumnWithColumnRequest
	from .clear import ClearRequest
	from .bounding_rect_with_anotherrange import BoundingRectWithAnotherRangeRequest
	from .format import FormatRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.workbook_range import WorkbookRange


class CellWithRowColumnRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/cell(row={row},column={column})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookRange:
		"""
		Invoke function cell
		Gets the range object containing the single cell based on row and column numbers. The cell can be outside the bounds of its parent range, so long as it's stays within the worksheet grid.
		Find more info here: https://learn.microsoft.com/graph/api/worksheet-cell?view=graph-rest-1.0
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


	def with_url(self, raw_url: str) -> CellWithRowColumnRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CellWithRowColumnRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CellWithRowColumnRequest(self.request_adapter, self.path_parameters)

	def format(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> FormatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .format import FormatRequest
		return FormatRequest(self.request_adapter, path_parameters)

	def bounding_rect_with_anotherrange(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		anotherRange: str,
	) -> BoundingRectWithAnotherRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if anotherRange is None:
			raise TypeError("anotherRange cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["anotherRange"] =  anotherRange

		from .bounding_rect_with_anotherrange import BoundingRectWithAnotherRangeRequest
		return BoundingRectWithAnotherRangeRequest(self.request_adapter, path_parameters)

	def clear(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> ClearRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .clear import ClearRequest
		return ClearRequest(self.request_adapter, path_parameters)

	def column_with_column(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		column1: int,
	) -> ColumnWithColumnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if column1 is None:
			raise TypeError("column1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["column1"] =  column1

		from .column_with_column import ColumnWithColumnRequest
		return ColumnWithColumnRequest(self.request_adapter, path_parameters)

	def columns_after(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> ColumnsAfterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .columns_after import ColumnsAfterRequest
		return ColumnsAfterRequest(self.request_adapter, path_parameters)

	def columns_after_with_count(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		count: int,
	) -> ColumnsAfterWithCountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if count is None:
			raise TypeError("count cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["count"] =  count

		from .columns_after_with_count import ColumnsAfterWithCountRequest
		return ColumnsAfterWithCountRequest(self.request_adapter, path_parameters)

	def columns_before(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> ColumnsBeforeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .columns_before import ColumnsBeforeRequest
		return ColumnsBeforeRequest(self.request_adapter, path_parameters)

	def columns_before_with_count(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		count: int,
	) -> ColumnsBeforeWithCountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if count is None:
			raise TypeError("count cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["count"] =  count

		from .columns_before_with_count import ColumnsBeforeWithCountRequest
		return ColumnsBeforeWithCountRequest(self.request_adapter, path_parameters)

	def delete(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> DeleteRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .delete import DeleteRequest
		return DeleteRequest(self.request_adapter, path_parameters)

	def entire_column(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> EntireColumnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .entire_column import EntireColumnRequest
		return EntireColumnRequest(self.request_adapter, path_parameters)

	def entire_row(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> EntireRowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .entire_row import EntireRowRequest
		return EntireRowRequest(self.request_adapter, path_parameters)

	def insert(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> InsertRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .insert import InsertRequest
		return InsertRequest(self.request_adapter, path_parameters)

	def intersection_with_anotherrange(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		anotherRange: str,
	) -> IntersectionWithAnotherRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if anotherRange is None:
			raise TypeError("anotherRange cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["anotherRange"] =  anotherRange

		from .intersection_with_anotherrange import IntersectionWithAnotherRangeRequest
		return IntersectionWithAnotherRangeRequest(self.request_adapter, path_parameters)

	def last_cell(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> LastCellRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .last_cell import LastCellRequest
		return LastCellRequest(self.request_adapter, path_parameters)

	def last_column(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> LastColumnRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .last_column import LastColumnRequest
		return LastColumnRequest(self.request_adapter, path_parameters)

	def last_row(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> LastRowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .last_row import LastRowRequest
		return LastRowRequest(self.request_adapter, path_parameters)

	def merge(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> MergeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .merge import MergeRequest
		return MergeRequest(self.request_adapter, path_parameters)

	def offset_range_with_rowoffset_columnoffset(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		rowOffset: int,
		columnOffset: int,
	) -> OffsetRangeWithRowOffsetColumnOffsetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if rowOffset is None:
			raise TypeError("rowOffset cannot be null.")
		if columnOffset is None:
			raise TypeError("columnOffset cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["rowOffset"] =  rowOffset
		path_parameters["columnOffset"] =  columnOffset

		from .offset_range_with_rowoffset_columnoffset import OffsetRangeWithRowOffsetColumnOffsetRequest
		return OffsetRangeWithRowOffsetColumnOffsetRequest(self.request_adapter, path_parameters)

	def resized_range_with_deltarows_deltacolumns(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		deltaRows: int,
		deltaColumns: int,
	) -> ResizedRangeWithDeltaRowsDeltaColumnsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if deltaRows is None:
			raise TypeError("deltaRows cannot be null.")
		if deltaColumns is None:
			raise TypeError("deltaColumns cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["deltaRows"] =  deltaRows
		path_parameters["deltaColumns"] =  deltaColumns

		from .resized_range_with_deltarows_deltacolumns import ResizedRangeWithDeltaRowsDeltaColumnsRequest
		return ResizedRangeWithDeltaRowsDeltaColumnsRequest(self.request_adapter, path_parameters)

	def row_with_row(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		row1: int,
	) -> RowWithRowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if row1 is None:
			raise TypeError("row1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["row1"] =  row1

		from .row_with_row import RowWithRowRequest
		return RowWithRowRequest(self.request_adapter, path_parameters)

	def rows_above(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> RowsAboveRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .rows_above import RowsAboveRequest
		return RowsAboveRequest(self.request_adapter, path_parameters)

	def rows_above_with_count(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		count: int,
	) -> RowsAboveWithCountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if count is None:
			raise TypeError("count cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["count"] =  count

		from .rows_above_with_count import RowsAboveWithCountRequest
		return RowsAboveWithCountRequest(self.request_adapter, path_parameters)

	def rows_below(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> RowsBelowRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .rows_below import RowsBelowRequest
		return RowsBelowRequest(self.request_adapter, path_parameters)

	def rows_below_with_count(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		count: int,
	) -> RowsBelowWithCountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if count is None:
			raise TypeError("count cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["count"] =  count

		from .rows_below_with_count import RowsBelowWithCountRequest
		return RowsBelowWithCountRequest(self.request_adapter, path_parameters)

	def unmerge(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> UnmergeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .unmerge import UnmergeRequest
		return UnmergeRequest(self.request_adapter, path_parameters)

	def used_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> UsedRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .used_range import UsedRangeRequest
		return UsedRangeRequest(self.request_adapter, path_parameters)

	def used_range_with_valuesonly(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
		valuesOnly: bool,
	) -> UsedRangeWithValuesOnlyRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")
		if valuesOnly is None:
			raise TypeError("valuesOnly cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column
		path_parameters["valuesOnly"] =  valuesOnly

		from .used_range_with_valuesonly import UsedRangeWithValuesOnlyRequest
		return UsedRangeWithValuesOnlyRequest(self.request_adapter, path_parameters)

	def visible_view(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> VisibleViewRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .visible_view import VisibleViewRequest
		return VisibleViewRequest(self.request_adapter, path_parameters)

	def sort(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> SortRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .sort import SortRequest
		return SortRequest(self.request_adapter, path_parameters)

	def worksheet(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		row: int,
		column: int,
	) -> WorksheetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if row is None:
			raise TypeError("row cannot be null.")
		if column is None:
			raise TypeError("column cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["row"] =  row
		path_parameters["column"] =  column

		from .worksheet import WorksheetRequest
		return WorksheetRequest(self.request_adapter, path_parameters)

