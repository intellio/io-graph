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
from iograph_models.models.create_link_post_request import Create_linkPostRequest
from iograph_models.models.permission import Permission
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class CreateLinkRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/createLink"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Create_linkPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Permission:
		"""
		Invoke action createLink
		You can use createLink action to share a DriveItem via a sharing link. The createLink action will create a new sharing link if the specified link type doesn't already exist for the calling application.
If a sharing link of the specified type already exists for the app, the existing sharing link will be returned. DriveItem resources inherit sharing permissions from their ancestors.
		Find more info here: https://learn.microsoft.com/graph/api/driveitem-createlink?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, Permission, error_mapping)


