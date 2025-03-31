# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.windows_updates_update_audience_by_id_post_request import Windows_updates_update_audience_by_idPostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class WindowsUpdatesUpdateAudienceByIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/deployments/{deployment%2Did}/audience/microsoft.graph.windowsUpdates.updateAudienceById", path_parameters)

	async def post(
		self,
		body: Windows_updates_update_audience_by_idPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action updateAudienceById
		Update the members and exclusions collections of a deploymentAudience with updatableAsset resources of the same type. Adding an azureADDevice to the members or exclusions collections of a deployment audience automatically creates a Microsoft Entra device object if it does not already exist. If the same updatableAsset gets included in the exclusions and members collections of a deploymentAudience, deployment will not apply to that asset. You can also use the method updateAudience to update the deploymentAudience.
		Find more info here: https://learn.microsoft.com/graph/api/windowsupdates-deploymentaudience-updateaudiencebyid?view=graph-rest-beta
		"""
		tags = ['admin.adminWindows']

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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> WindowsUpdatesUpdateAudienceByIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: WindowsUpdatesUpdateAudienceByIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return WindowsUpdatesUpdateAudienceByIdRequest(self.request_adapter, self.path_parameters)

