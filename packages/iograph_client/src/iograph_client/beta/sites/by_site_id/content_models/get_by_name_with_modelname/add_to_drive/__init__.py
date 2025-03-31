# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.add_to_drive_post_request import Add_to_drivePostRequest
from iograph_models.beta.content_model_usage import ContentModelUsage
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AddToDriveRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/contentModels/getByName(modelName='{modelName}')/addToDrive", path_parameters)

	async def post(
		self,
		body: Add_to_drivePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContentModelUsage:
		"""
		Invoke action addToDrive
		Apply a contentModel to SharePoint document libraries. For an existing model that's already trained, this action automatically processes new documents that are added to the SharePoint libraries.
		Find more info here: https://learn.microsoft.com/graph/api/contentmodel-addtodrive?view=graph-rest-beta
		"""
		tags = ['sites.site.Actions']

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
		return await self.request_adapter.send_async(request_info, ContentModelUsage, error_mapping)


	def with_url(self, raw_url: str) -> AddToDriveRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AddToDriveRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AddToDriveRequest(self.request_adapter, self.path_parameters)

