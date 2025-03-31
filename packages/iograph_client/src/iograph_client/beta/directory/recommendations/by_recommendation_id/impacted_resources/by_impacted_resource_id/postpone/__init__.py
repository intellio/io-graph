# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.impacted_resource import ImpactedResource
from iograph_models.beta.postpone_post_request import PostponePostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class PostponeRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/recommendations/{recommendation%2Did}/impactedResources/{impactedResource%2Did}/postpone", path_parameters)

	async def post(
		self,
		body: PostponePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ImpactedResource:
		"""
		Invoke action postpone
		Postpone action on an impactedResource object to a specified future date and time by marking its status as postponed. On the specified date and time, Microsoft Entra ID will automatically mark the status of the impactedResource object to active.
		Find more info here: https://learn.microsoft.com/graph/api/impactedresource-postpone?view=graph-rest-beta
		"""
		tags = ['directory.recommendation']

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
		return await self.request_adapter.send_async(request_info, ImpactedResource, error_mapping)


	def with_url(self, raw_url: str) -> PostponeRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PostponeRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PostponeRequest(self.request_adapter, self.path_parameters)

