# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.models.upload_session import UploadSession
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.create_upload_session_post_request import Create_upload_sessionPostRequest


class CreateUploadSessionRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/print/printers/{printer%2Did}/jobs/{printJob%2Did}/documents/{printDocument%2Did}/createUploadSession"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Create_upload_sessionPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UploadSession:
		"""
		Invoke action createUploadSession
		Create an upload session that allows an app to iteratively upload ranges of a binary file linked to the print document. As part of the response, this action returns an upload URL that can be used in subsequent sequential PUT queries. Request headers for each PUT operation can be used to specify the exact range of bytes to be uploaded. This allows transfer to be resumed, in case the network connection is dropped during upload. 
		Find more info here: https://learn.microsoft.com/graph/api/printdocument-createuploadsession?view=graph-rest-1.0
		"""
		tags = ['print.printer']

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


