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
	from .refresh_all import RefreshAllRequest
	from .count import CountRequest
	from .by_workbook_pivot_table_id import ByWorkbookPivotTableIdRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_pivot_table_collection_response import WorkbookPivotTableCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.workbook_pivot_table import WorkbookPivotTable


class PivotTablesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/pivotTables", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookPivotTableCollectionResponse:
		"""
		Get pivotTables from drives
		The list of piot tables that are part of the worksheet.
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
		return await self.request_adapter.send_async(request_info, WorkbookPivotTableCollectionResponse, error_mapping)

	async def post(
		self,
		body: WorkbookPivotTable,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookPivotTable:
		"""
		Create new navigation property to pivotTables for drives
		
		"""
		tags = ['drives.driveItem']

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
		return await self.request_adapter.send_async(request_info, WorkbookPivotTable, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PivotTablesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PivotTablesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PivotTablesRequest(self.request_adapter, self.path_parameters)

	def by_workbook_pivot_table_id(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookPivotTable_id: str,
	) -> ByWorkbookPivotTableIdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookPivotTable_id is None:
			raise TypeError("workbookPivotTable_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookPivotTable%2Did"] =  workbookPivotTable_id

		from .by_workbook_pivot_table_id import ByWorkbookPivotTableIdRequest
		return ByWorkbookPivotTableIdRequest(self.request_adapter, path_parameters)

	def count(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
	) -> CountRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def refresh_all(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
	) -> RefreshAllRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id

		from .refresh_all import RefreshAllRequest
		return RefreshAllRequest(self.request_adapter, path_parameters)

