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
	from .content_stream import ContentStreamRequest
	from .content import ContentRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.drive_item import DriveItem
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByDriveItemId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/children/{driveItem%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DriveItem:
		"""
		Get children from drives
		Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.
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

	def with_url(self, raw_url: str) -> ByDriveItemId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDriveItemId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDriveItemId1Request(self.request_adapter, self.path_parameters)

	def content(self,
		drive_id: str,
		driveItem_id: str,
		driveItem_id1: str,
	) -> ContentRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if driveItem_id1 is None:
			raise TypeError("driveItem_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["driveItem%2Did1"] =  driveItem_id1

		from .content import ContentRequest
		return ContentRequest(self.request_adapter, path_parameters)

	def content_stream(self,
		drive_id: str,
		driveItem_id: str,
		driveItem_id1: str,
	) -> ContentStreamRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if driveItem_id is None:
			raise TypeError("driveItem_id cannot be null.")
		if driveItem_id1 is None:
			raise TypeError("driveItem_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["driveItem%2Did"] =  driveItem_id
		path_parameters["driveItem%2Did1"] =  driveItem_id1

		from .content_stream import ContentStreamRequest
		return ContentStreamRequest(self.request_adapter, path_parameters)

