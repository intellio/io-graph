# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .content import ContentRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.v1.drive_item import DriveItem
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class DriveItemRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/analytics/itemActivityStats/{itemActivityStat%2Did}/activities/{itemActivity%2Did}/driveItem", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DriveItem:
		"""
		Get driveItem from drives
		Exposes the driveItem that was the target of this activity.
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
		return await self.request_adapter.send_async(request_info, DriveItem, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> DriveItemRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DriveItemRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DriveItemRequest(self.request_adapter, self.path_parameters)

	def content(self,
		drive_id: str,
		driveItem_id: str,
		itemActivityStat_id: str,
		itemActivity_id: str,
	) -> ContentRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if itemActivityStat_id is None:
			raise TypeError("itemActivityStat_id cannot be null.")
		if itemActivity_id is None:
			raise TypeError("itemActivity_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["itemActivityStat%2Did"] =  itemActivityStat_id
		path_parameters["itemActivity%2Did"] =  itemActivity_id

		from .content import ContentRequest
		return ContentRequest(self.request_adapter, path_parameters)

