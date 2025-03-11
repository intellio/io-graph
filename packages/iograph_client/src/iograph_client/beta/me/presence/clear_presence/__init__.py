# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.clear_presence_post_request import Clear_presencePostRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ClearPresenceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/presence/clearPresence", path_parameters)

	async def post(
		self,
		body: Clear_presencePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action clearPresence
		Clear a presence session of an application for a user. If it is the user's only presence session, a successful clearPresence changes the user's presence to Offline/Offline. Read more about presence sessions and their time-out and expiration. 
		Find more info here: https://learn.microsoft.com/graph/api/presence-clearpresence?view=graph-rest-beta
		"""
		tags = ['me.presence']

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


	def with_url(self, raw_url: str) -> ClearPresenceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ClearPresenceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ClearPresenceRequest(self.request_adapter, self.path_parameters)

