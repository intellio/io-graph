# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .clear import ClearRequest
	from .apply_values_filter import ApplyValuesFilterRequest
	from .apply_top_percent_filter import ApplyTopPercentFilterRequest
	from .apply_top_items_filter import ApplyTopItemsFilterRequest
	from .apply_icon_filter import ApplyIconFilterRequest
	from .apply_font_color_filter import ApplyFontColorFilterRequest
	from .apply_dynamic_filter import ApplyDynamicFilterRequest
	from .apply_custom_filter import ApplyCustomFilterRequest
	from .apply_cell_color_filter import ApplyCellColorFilterRequest
	from .apply_bottom_percent_filter import ApplyBottomPercentFilterRequest
	from .apply_bottom_items_filter import ApplyBottomItemsFilterRequest
	from .apply import ApplyRequest
	from ..............request_adapter import HttpxRequestAdapter
from iograph_models.v1.workbook_filter import WorkbookFilter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class FilterRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/tables/{workbookTable%2Did}/columns/{workbookTableColumn%2Did}/filter", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookFilter:
		"""
		Get filter from drives
		The filter applied to the column. Read-only.
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
		return await self.request_adapter.send_async(request_info, WorkbookFilter, error_mapping)

	async def patch(
		self,
		body: WorkbookFilter,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookFilter:
		"""
		Update the navigation property filter in drives
		
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
		return await self.request_adapter.send_async(request_info, WorkbookFilter, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property filter for drives
		
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



	def with_url(self, raw_url: str) -> FilterRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: FilterRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return FilterRequest(self.request_adapter, self.path_parameters)

	def apply(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply import ApplyRequest
		return ApplyRequest(self.request_adapter, path_parameters)

	def apply_bottom_items_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyBottomItemsFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_bottom_items_filter import ApplyBottomItemsFilterRequest
		return ApplyBottomItemsFilterRequest(self.request_adapter, path_parameters)

	def apply_bottom_percent_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyBottomPercentFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_bottom_percent_filter import ApplyBottomPercentFilterRequest
		return ApplyBottomPercentFilterRequest(self.request_adapter, path_parameters)

	def apply_cell_color_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyCellColorFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_cell_color_filter import ApplyCellColorFilterRequest
		return ApplyCellColorFilterRequest(self.request_adapter, path_parameters)

	def apply_custom_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyCustomFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_custom_filter import ApplyCustomFilterRequest
		return ApplyCustomFilterRequest(self.request_adapter, path_parameters)

	def apply_dynamic_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyDynamicFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_dynamic_filter import ApplyDynamicFilterRequest
		return ApplyDynamicFilterRequest(self.request_adapter, path_parameters)

	def apply_font_color_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyFontColorFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_font_color_filter import ApplyFontColorFilterRequest
		return ApplyFontColorFilterRequest(self.request_adapter, path_parameters)

	def apply_icon_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyIconFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_icon_filter import ApplyIconFilterRequest
		return ApplyIconFilterRequest(self.request_adapter, path_parameters)

	def apply_top_items_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyTopItemsFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_top_items_filter import ApplyTopItemsFilterRequest
		return ApplyTopItemsFilterRequest(self.request_adapter, path_parameters)

	def apply_top_percent_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyTopPercentFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_top_percent_filter import ApplyTopPercentFilterRequest
		return ApplyTopPercentFilterRequest(self.request_adapter, path_parameters)

	def apply_values_filter(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ApplyValuesFilterRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .apply_values_filter import ApplyValuesFilterRequest
		return ApplyValuesFilterRequest(self.request_adapter, path_parameters)

	def clear(self,
		drive_id: str,
		driveItem_id: str,
		workbookWorksheet_id: str,
		workbookTable_id: str,
		workbookTableColumn_id: str,
	) -> ClearRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookWorksheet_id is None:
			raise TypeError("workbookWorksheet_id cannot be null.")
		if workbookTable_id is None:
			raise TypeError("workbookTable_id cannot be null.")
		if workbookTableColumn_id is None:
			raise TypeError("workbookTableColumn_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookWorksheet%2Did"] =  workbookWorksheet_id
		path_parameters["workbookTable%2Did"] =  workbookTable_id
		path_parameters["workbookTableColumn%2Did"] =  workbookTableColumn_id

		from .clear import ClearRequest
		return ClearRequest(self.request_adapter, path_parameters)

