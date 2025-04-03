# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .total_row_range import TotalRowRangeRequest
	from .range import RangeRequest
	from .header_row_range import HeaderRowRangeRequest
	from .data_body_range import DataBodyRangeRequest
	from .filter import FilterRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.workbook_table_column import WorkbookTableColumn


class ItemAtWithIndexRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tables/{workbookTable%2Did}/columns/itemAt(index={index})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookTableColumn:
		"""
		Invoke function itemAt
		Gets a column based on its position in the collection.
		Find more info here: https://learn.microsoft.com/graph/api/tablecolumncollection-itemat?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, WorkbookTableColumn, error_mapping)


	def with_url(self, raw_url: str) -> ItemAtWithIndexRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemAtWithIndexRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemAtWithIndexRequest(self.request_adapter, self.path_parameters)

	def filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
		index: int,
	) -> FilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["index"] =  index

		from .filter import FilterRequest
		return FilterRequest(self.request_adapter, path_parameters)

	def data_body_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
		index: int,
	) -> DataBodyRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["index"] =  index

		from .data_body_range import DataBodyRangeRequest
		return DataBodyRangeRequest(self.request_adapter, path_parameters)

	def header_row_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
		index: int,
	) -> HeaderRowRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["index"] =  index

		from .header_row_range import HeaderRowRangeRequest
		return HeaderRowRangeRequest(self.request_adapter, path_parameters)

	def range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
		index: int,
	) -> RangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["index"] =  index

		from .range import RangeRequest
		return RangeRequest(self.request_adapter, path_parameters)

	def total_row_range(self,
		drive_id: str,
		driveItem_id: str,
		workbookTable_id: str,
		index: int,
	) -> TotalRowRangeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["index"] =  index

		from .total_row_range import TotalRowRangeRequest
		return TotalRowRangeRequest(self.request_adapter, path_parameters)

