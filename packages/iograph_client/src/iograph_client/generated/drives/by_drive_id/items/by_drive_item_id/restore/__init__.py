# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.restore_post_request import RestorePostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.drive_item import DriveItem


class RestoreRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/restore"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: RestorePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DriveItem:
		"""
		Invoke action restore
		Restore a driveItem that has been deleted and is currently in the recycle bin. NOTE: This functionality is currently only available for OneDrive Personal.
		Find more info here: https://learn.microsoft.com/graph/api/driveitem-restore?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, DriveItem, error_mapping)


