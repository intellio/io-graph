# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .title import TitleRequest
	from .minor_gridlines import MinorGridlinesRequest
	from .major_gridlines import MajorGridlinesRequest
	from .format import FormatRequest
	from .............request_adapter import HttpxRequestAdapter
from iograph_models.v1.workbook_chart_axis import WorkbookChartAxis
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class CategoryAxisRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/axes/categoryAxis", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookChartAxis:
		"""
		Get categoryAxis from drives
		Represents the category axis in a chart. Read-only.
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
		return await self.request_adapter.send_async(request_info, WorkbookChartAxis, error_mapping)

	async def patch(
		self,
		body: WorkbookChartAxis,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookChartAxis:
		"""
		Update the navigation property categoryAxis in drives
		
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
		return await self.request_adapter.send_async(request_info, WorkbookChartAxis, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property categoryAxis for drives
		
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



	def with_url(self, raw_url: str) -> CategoryAxisRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: CategoryAxisRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return CategoryAxisRequest(self.request_adapter, self.path_parameters)

	def format(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookChart_id: str,
	) -> FormatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookChart_id is None:
			raise TypeError("workbookChart_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookChart%2Did"] =  workbookChart_id

		from .format import FormatRequest
		return FormatRequest(self.request_adapter, path_parameters)

	def major_gridlines(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookChart_id: str,
	) -> MajorGridlinesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookChart_id is None:
			raise TypeError("workbookChart_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookChart%2Did"] =  workbookChart_id

		from .major_gridlines import MajorGridlinesRequest
		return MajorGridlinesRequest(self.request_adapter, path_parameters)

	def minor_gridlines(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookChart_id: str,
	) -> MinorGridlinesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookChart_id is None:
			raise TypeError("workbookChart_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookChart%2Did"] =  workbookChart_id

		from .minor_gridlines import MinorGridlinesRequest
		return MinorGridlinesRequest(self.request_adapter, path_parameters)

	def title(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookChart_id: str,
	) -> TitleRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookChart_id is None:
			raise TypeError("workbookChart_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookChart%2Did"] =  workbookChart_id

		from .title import TitleRequest
		return TitleRequest(self.request_adapter, path_parameters)

