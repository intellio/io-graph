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
	from .image import ImageRequest
	from .legend import LegendRequest
	from .format import FormatRequest
	from .data_labels import DataLabelsRequest
	from .axes import AxesRequest
	from ...........request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_chart import WorkbookChart
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ItemRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/item(name='{name}')", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookChart:
		"""
		Invoke function item
		
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


	def with_url(self, raw_url: str) -> ItemRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ItemRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ItemRequest(self.request_adapter, self.path_parameters)

	def axes(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> AxesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .axes import AxesRequest
		return AxesRequest(self.request_adapter, path_parameters)

	def data_labels(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> DataLabelsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .data_labels import DataLabelsRequest
		return DataLabelsRequest(self.request_adapter, path_parameters)

	def format(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> FormatRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .format import FormatRequest
		return FormatRequest(self.request_adapter, path_parameters)

	def legend(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> LegendRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .legend import LegendRequest
		return LegendRequest(self.request_adapter, path_parameters)

	def image(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> ImageRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .image import ImageRequest
		return ImageRequest(self.request_adapter, path_parameters)

	def set_data(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> SetDataRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .set_data import SetDataRequest
		return SetDataRequest(self.request_adapter, path_parameters)

	def set_position(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> SetPositionRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .set_position import SetPositionRequest
		return SetPositionRequest(self.request_adapter, path_parameters)

	def series(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> SeriesRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .series import SeriesRequest
		return SeriesRequest(self.request_adapter, path_parameters)

	def title(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> TitleRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .title import TitleRequest
		return TitleRequest(self.request_adapter, path_parameters)

	def worksheet(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		name: str,
	) -> WorksheetRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if name is None:
			raise TypeError("name cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["name"] =  name

		from .worksheet import WorksheetRequest
		return WorksheetRequest(self.request_adapter, path_parameters)

