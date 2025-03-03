# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .add_formula_local import AddFormulaLocalRequest
	from .add import AddRequest
	from .count import CountRequest
	from .by_workbook_named_item_id import ByWorkbookNamedItemIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.models.workbook_named_item_collection_response import WorkbookNamedItemCollectionResponse
from iograph_models.models.workbook_named_item import WorkbookNamedItem
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class NamesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/names", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> WorkbookNamedItemCollectionResponse:
		"""
		Get names from drives
		Represents a collection of workbooks scoped named items (named ranges and constants). Read-only.
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
		return await self.request_adapter.send_async(request_info, WorkbookNamedItemCollectionResponse, error_mapping)

	async def post(
		self,
		body: WorkbookNamedItem,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> WorkbookNamedItem:
		"""
		Create new navigation property to names for drives
		
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
		return await self.request_adapter.send_async(request_info, WorkbookNamedItem, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> NamesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: NamesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return NamesRequest(self.request_adapter, self.path_parameters)

	def by_workbook_named_item_id(self,
		drive_id: str,
		driveItem_id: str,
		workbookNamedItem_id: str,
	) -> ByWorkbookNamedItemIdRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if workbookNamedItem_id is None:
			raise TypeError("workbookNamedItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["workbookNamedItem%2Did"] =  workbookNamedItem_id

		from .by_workbook_named_item_id import ByWorkbookNamedItemIdRequest
		return ByWorkbookNamedItemIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def add(self,
	) -> AddRequest:
		from .add import AddRequest
		return AddRequest(self.request_adapter, self.path_parameters)

	@property
	def add_formula_local(self,
	) -> AddFormulaLocalRequest:
		from .add_formula_local import AddFormulaLocalRequest
		return AddFormulaLocalRequest(self.request_adapter, self.path_parameters)

