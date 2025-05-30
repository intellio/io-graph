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
	from .worksheet import WorksheetRequest
	from .title import TitleRequest
	from .series import SeriesRequest
	from .set_position import SetPositionRequest
	from .set_data import SetDataRequest
	from .image_with_width import ImageWithWidthRequest
	from .image_with_width_height import ImageWithWidthHeightRequest
	from .image_with_width_height_fittingmode import ImageWithWidthHeightFittingModeRequest
	from .image import ImageRequest
	from .legend import LegendRequest
	from .format import FormatRequest
	from .data_labels import DataLabelsRequest
	from .axes import AxesRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.workbook_chart import WorkbookChart


class ItemAtWithIndexRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/itemAt(index={index})", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookChart:
		"""
		Invoke function itemAt
		Gets a chart based on its position in the collection.
		Find more info here: https://learn.microsoft.com/graph/api/chartcollection-itemat?view=graph-rest-beta
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


	def with_url(self, raw_url: str) -> ItemAtWithIndexRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemAtWithIndexRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemAtWithIndexRequest(self.request_adapter, self.path_parameters)

	def axes(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> AxesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .axes import AxesRequest
		return AxesRequest(self.request_adapter, path_parameters)

	def data_labels(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> DataLabelsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .data_labels import DataLabelsRequest
		return DataLabelsRequest(self.request_adapter, path_parameters)

	def format(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> FormatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .format import FormatRequest
		return FormatRequest(self.request_adapter, path_parameters)

	def legend(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> LegendRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .legend import LegendRequest
		return LegendRequest(self.request_adapter, path_parameters)

	def image(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> ImageRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .image import ImageRequest
		return ImageRequest(self.request_adapter, path_parameters)

	def image_with_width_height_fittingmode(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
		width: int,
		height: int,
		fittingMode: str,
	) -> ImageWithWidthHeightFittingModeRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")
		if width is None:
			raise TypeError("width cannot be null.")
		if height is None:
			raise TypeError("height cannot be null.")
		if fittingMode is None:
			raise TypeError("fittingMode cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index
		path_parameters["width"] =  width
		path_parameters["height"] =  height
		path_parameters["fittingMode"] =  fittingMode

		from .image_with_width_height_fittingmode import ImageWithWidthHeightFittingModeRequest
		return ImageWithWidthHeightFittingModeRequest(self.request_adapter, path_parameters)

	def image_with_width_height(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
		width: int,
		height: int,
	) -> ImageWithWidthHeightRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")
		if width is None:
			raise TypeError("width cannot be null.")
		if height is None:
			raise TypeError("height cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index
		path_parameters["width"] =  width
		path_parameters["height"] =  height

		from .image_with_width_height import ImageWithWidthHeightRequest
		return ImageWithWidthHeightRequest(self.request_adapter, path_parameters)

	def image_with_width(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
		width: int,
	) -> ImageWithWidthRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")
		if width is None:
			raise TypeError("width cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index
		path_parameters["width"] =  width

		from .image_with_width import ImageWithWidthRequest
		return ImageWithWidthRequest(self.request_adapter, path_parameters)

	def set_data(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> SetDataRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .set_data import SetDataRequest
		return SetDataRequest(self.request_adapter, path_parameters)

	def set_position(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> SetPositionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .set_position import SetPositionRequest
		return SetPositionRequest(self.request_adapter, path_parameters)

	def series(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> SeriesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .series import SeriesRequest
		return SeriesRequest(self.request_adapter, path_parameters)

	def title(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> TitleRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .title import TitleRequest
		return TitleRequest(self.request_adapter, path_parameters)

	def worksheet(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		index: int,
	) -> WorksheetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if index is None:
			raise TypeError("index cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["index"] =  index

		from .worksheet import WorksheetRequest
		return WorksheetRequest(self.request_adapter, path_parameters)

