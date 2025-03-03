# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .set_user_preferred_presence import SetUserPreferredPresenceRequest
	from .set_status_message import SetStatusMessageRequest
	from .set_presence import SetPresenceRequest
	from .clear_user_preferred_presence import ClearUserPreferredPresenceRequest
	from .clear_presence import ClearPresenceRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.presence import Presence
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class PresenceRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/presence", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Presence:
		"""
		Get presence
		Get a user's presence information.
		Find more info here: https://learn.microsoft.com/graph/api/presence-get?view=graph-rest-1.0
		"""
		tags = ['me.presence']

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
		return await self.request_adapter.send_async(request_info, Presence, error_mapping)

	async def patch(
		self,
		body: Presence,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Presence:
		"""
		Update the navigation property presence in me
		
		"""
		tags = ['me.presence']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, Presence, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property presence for me
		
		"""
		tags = ['me.presence']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> PresenceRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PresenceRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PresenceRequest(self.request_adapter, self.path_parameters)

	@property
	def clear_presence(self,
	) -> ClearPresenceRequest:
		from .clear_presence import ClearPresenceRequest
		return ClearPresenceRequest(self.request_adapter, self.path_parameters)

	@property
	def clear_user_preferred_presence(self,
	) -> ClearUserPreferredPresenceRequest:
		from .clear_user_preferred_presence import ClearUserPreferredPresenceRequest
		return ClearUserPreferredPresenceRequest(self.request_adapter, self.path_parameters)

	@property
	def set_presence(self,
	) -> SetPresenceRequest:
		from .set_presence import SetPresenceRequest
		return SetPresenceRequest(self.request_adapter, self.path_parameters)

	@property
	def set_status_message(self,
	) -> SetStatusMessageRequest:
		from .set_status_message import SetStatusMessageRequest
		return SetStatusMessageRequest(self.request_adapter, self.path_parameters)

	@property
	def set_user_preferred_presence(self,
	) -> SetUserPreferredPresenceRequest:
		from .set_user_preferred_presence import SetUserPreferredPresenceRequest
		return SetUserPreferredPresenceRequest(self.request_adapter, self.path_parameters)

