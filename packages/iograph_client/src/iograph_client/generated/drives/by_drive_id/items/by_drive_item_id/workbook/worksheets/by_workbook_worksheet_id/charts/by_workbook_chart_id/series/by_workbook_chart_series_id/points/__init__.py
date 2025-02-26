# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .by_workbook_chart_point_id import ByWorkbookChartPointIdRequest
	from ..............request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_chart_point_collection_response import WorkbookChartPointCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.workbook_chart_point import WorkbookChartPoint


class PointsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/series/{workbookChartSeries%2Did}/points"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookChartPointCollectionResponse:
		"""
		Get points from drives
		A collection of all points in the series. Read-only.
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
		return await self.request_adapter.send_async(request_info, WorkbookChartPointCollectionResponse, error_mapping)

	async def post(
		self,
		body: WorkbookChartPoint,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookChartPoint:
		"""
		Create new navigation property to points for drives
		
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
		return await self.request_adapter.send_async(request_info, WorkbookChartPoint, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_workbook_chart_point_id(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookChart_id: str,
		workbookChartSeries_id: str,
		workbookChartPoint_id: str,
	) -> ByWorkbookChartPointIdRequest:
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
		if workbookChartPoint_id is None:
			raise TypeError("workbookChartPoint_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookChart%2Did"] =  workbookChart_id
		path_parameters["workbookChartSeries%2Did"] =  workbookChartSeries_id
		path_parameters["workbookChartPoint%2Did"] =  workbookChartPoint_id

		from .by_workbook_chart_point_id import ByWorkbookChartPointIdRequest
		return ByWorkbookChartPointIdRequest(self.request_adapter, path_parameters)

