# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
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
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.workbook_filter import WorkbookFilter


class FilterRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tables/{workbookTable%2Did}/columns/{workbookTableColumn%2Did}/filter"
		self.path_parameters: dict[str, Any] = path_parameters

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



	@property
	def apply(self,
	) -> ApplyRequest:
		from .apply import ApplyRequest
		return ApplyRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_bottom_items_filter(self,
	) -> ApplyBottomItemsFilterRequest:
		from .apply_bottom_items_filter import ApplyBottomItemsFilterRequest
		return ApplyBottomItemsFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_bottom_percent_filter(self,
	) -> ApplyBottomPercentFilterRequest:
		from .apply_bottom_percent_filter import ApplyBottomPercentFilterRequest
		return ApplyBottomPercentFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_cell_color_filter(self,
	) -> ApplyCellColorFilterRequest:
		from .apply_cell_color_filter import ApplyCellColorFilterRequest
		return ApplyCellColorFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_custom_filter(self,
	) -> ApplyCustomFilterRequest:
		from .apply_custom_filter import ApplyCustomFilterRequest
		return ApplyCustomFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_dynamic_filter(self,
	) -> ApplyDynamicFilterRequest:
		from .apply_dynamic_filter import ApplyDynamicFilterRequest
		return ApplyDynamicFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_font_color_filter(self,
	) -> ApplyFontColorFilterRequest:
		from .apply_font_color_filter import ApplyFontColorFilterRequest
		return ApplyFontColorFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_icon_filter(self,
	) -> ApplyIconFilterRequest:
		from .apply_icon_filter import ApplyIconFilterRequest
		return ApplyIconFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_top_items_filter(self,
	) -> ApplyTopItemsFilterRequest:
		from .apply_top_items_filter import ApplyTopItemsFilterRequest
		return ApplyTopItemsFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_top_percent_filter(self,
	) -> ApplyTopPercentFilterRequest:
		from .apply_top_percent_filter import ApplyTopPercentFilterRequest
		return ApplyTopPercentFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def apply_values_filter(self,
	) -> ApplyValuesFilterRequest:
		from .apply_values_filter import ApplyValuesFilterRequest
		return ApplyValuesFilterRequest(self.request_adapter, self.path_parameters)

	@property
	def clear(self,
	) -> ClearRequest:
		from .clear import ClearRequest
		return ClearRequest(self.request_adapter, self.path_parameters)

