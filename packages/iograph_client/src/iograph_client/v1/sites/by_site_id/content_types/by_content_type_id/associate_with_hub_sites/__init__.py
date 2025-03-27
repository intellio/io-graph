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
from iograph_models.v1.associate_with_hub_sites_post_request import Associate_with_hub_sitesPostRequest
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class AssociateWithHubSitesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/contentTypes/{contentType%2Did}/associateWithHubSites", path_parameters)

	async def post(
		self,
		body: Associate_with_hub_sitesPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action associateWithHubSites
		Associate a published content type present in a content type hub with a list of hub sites.
		Find more info here: https://learn.microsoft.com/graph/api/contenttype-associatewithhubsites?view=graph-rest-1.0
		"""
		tags = ['sites.contentType']

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


	def with_url(self, raw_url: str) -> AssociateWithHubSitesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssociateWithHubSitesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssociateWithHubSitesRequest(self.request_adapter, self.path_parameters)

