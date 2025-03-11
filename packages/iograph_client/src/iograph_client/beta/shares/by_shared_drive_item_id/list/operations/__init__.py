# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_rich_long_running_operation_id import ByRichLongRunningOperationIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.rich_long_running_operation import RichLongRunningOperation
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.rich_long_running_operation_collection_response import RichLongRunningOperationCollectionResponse


class OperationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/shares/{sharedDriveItem%2Did}/list/operations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RichLongRunningOperationCollectionResponse:
		"""
		Get operations from shares
		The collection of long-running operations on the list.
		"""
		tags = ['shares.list']

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
		return await self.request_adapter.send_async(request_info, RichLongRunningOperationCollectionResponse, error_mapping)

	async def post(
		self,
		body: RichLongRunningOperation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RichLongRunningOperation:
		"""
		Create new navigation property to operations for shares
		
		"""
		tags = ['shares.list']

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
		return await self.request_adapter.send_async(request_info, RichLongRunningOperation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> OperationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OperationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OperationsRequest(self.request_adapter, self.path_parameters)

	def by_rich_long_running_operation_id(self,
		sharedDriveItem_id: str,
		richLongRunningOperation_id: str,
	) -> ByRichLongRunningOperationIdRequest:
		if sharedDriveItem_id is None:
			raise TypeError("sharedDriveItem_id cannot be null.")
		if richLongRunningOperation_id is None:
			raise TypeError("richLongRunningOperation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedDriveItem%2Did"] =  sharedDriveItem_id
		path_parameters["richLongRunningOperation%2Did"] =  richLongRunningOperation_id

		from .by_rich_long_running_operation_id import ByRichLongRunningOperationIdRequest
		return ByRichLongRunningOperationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		sharedDriveItem_id: str,
	) -> CountRequest:
		if sharedDriveItem_id is None:
			raise TypeError("sharedDriveItem_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["sharedDriveItem%2Did"] =  sharedDriveItem_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

