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
from iograph_models.models.upload_session import UploadSession
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.create_upload_session_post_request import Create_upload_sessionPostRequest


class CreateUploadSessionRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/createUploadSession"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Create_upload_sessionPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UploadSession:
		"""
		Invoke action createUploadSession
		
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
		return await self.request_adapter.send_async(request_info, UploadSession, error_mapping)


