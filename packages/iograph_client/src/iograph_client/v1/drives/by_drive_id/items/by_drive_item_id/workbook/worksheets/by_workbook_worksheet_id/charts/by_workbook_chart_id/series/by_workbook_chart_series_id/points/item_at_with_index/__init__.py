# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .format import FormatRequest
	from ...............request_adapter import HttpxRequestAdapter
from iograph_models.v1.workbook_chart_point import WorkbookChartPoint
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ItemAtWithIndexRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/series/{workbookChartSeries%2Did}/points/itemAt(index={index})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookChartPoint:
		"""
		Invoke function itemAt
		Retrieve a point based on its position within the series.
		Find more info here: https://learn.microsoft.com/graph/api/chartpointscollection-itemat?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, WorkbookChartPoint, error_mapping)


	def with_url(self, raw_url: str) -> ItemAtWithIndexRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemAtWithIndexRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemAtWithIndexRequest(self.request_adapter, self.path_parameters)

	def format(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookChart_id: str,
		workbookChartSeries_id: str,
		index: int,
	) -> FormatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookChart_id is None:
			raise TypeError("workbookChart_id cannot be null.")
		if workbookChartSeries_id is None:
			raise TypeError("workbookChartSeries_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookChart%2Did"] =  workbookChart_id
		path_parameters["workbookChartSeries%2Did"] =  workbookChartSeries_id
		path_parameters["index"] =  index

		from .format import FormatRequest
		return FormatRequest(self.request_adapter, path_parameters)

