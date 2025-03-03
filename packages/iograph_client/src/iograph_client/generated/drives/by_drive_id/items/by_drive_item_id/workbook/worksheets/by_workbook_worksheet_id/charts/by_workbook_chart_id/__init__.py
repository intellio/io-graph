# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .worksheet import WorksheetRequest
	from .title import TitleRequest
	from .series import SeriesRequest
	from .set_position import SetPositionRequest
	from .set_data import SetDataRequest
	from .legend import LegendRequest
	from .format import FormatRequest
	from .data_labels import DataLabelsRequest
	from .axes import AxesRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_chart import WorkbookChart
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByWorkbookChartIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookChart:
		"""
		Get charts from drives
		The list of charts that are part of the worksheet. Read-only.
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
		return await self.request_adapter.send_async(request_info, WorkbookChart, error_mapping)

	async def patch(
		self,
		body: WorkbookChart,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookChart:
		"""
		Update the navigation property charts in drives
		
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
		return await self.request_adapter.send_async(request_info, WorkbookChart, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property charts for drives
		
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



	def with_url(self, raw_url: str) -> ByWorkbookChartIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByWorkbookChartIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByWorkbookChartIdRequest(self.request_adapter, self.path_parameters)

	@property
	def axes(self,
	) -> AxesRequest:
		from .axes import AxesRequest
		return AxesRequest(self.request_adapter, self.path_parameters)

	@property
	def data_labels(self,
	) -> DataLabelsRequest:
		from .data_labels import DataLabelsRequest
		return DataLabelsRequest(self.request_adapter, self.path_parameters)

	@property
	def format(self,
	) -> FormatRequest:
		from .format import FormatRequest
		return FormatRequest(self.request_adapter, self.path_parameters)

	@property
	def legend(self,
	) -> LegendRequest:
		from .legend import LegendRequest
		return LegendRequest(self.request_adapter, self.path_parameters)

	@property
	def set_data(self,
	) -> SetDataRequest:
		from .set_data import SetDataRequest
		return SetDataRequest(self.request_adapter, self.path_parameters)

	@property
	def set_position(self,
	) -> SetPositionRequest:
		from .set_position import SetPositionRequest
		return SetPositionRequest(self.request_adapter, self.path_parameters)

	@property
	def series(self,
	) -> SeriesRequest:
		from .series import SeriesRequest
		return SeriesRequest(self.request_adapter, self.path_parameters)

	@property
	def title(self,
	) -> TitleRequest:
		from .title import TitleRequest
		return TitleRequest(self.request_adapter, self.path_parameters)

	@property
	def worksheet(self,
	) -> WorksheetRequest:
		from .worksheet import WorksheetRequest
		return WorksheetRequest(self.request_adapter, self.path_parameters)

