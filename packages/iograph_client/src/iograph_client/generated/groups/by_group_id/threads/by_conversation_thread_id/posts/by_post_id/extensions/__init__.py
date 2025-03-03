# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_extension_id import ByExtensionIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.models.extension_collection_response import ExtensionCollectionResponse
from iograph_models.models.extension import Extension
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ExtensionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/threads/{conversationThread%2Did}/posts/{post%2Did}/extensions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExtensionCollectionResponse:
		"""
		Get open extension
		Get an open extension (openTypeExtension object) identified by name or fully qualified name. The table in the Permissions section lists the resources that support open extensions. The following table lists the three scenarios where you can get an open extension from a supported resource instance.
		"""
		tags = ['groups.conversationThread']

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
		return await self.request_adapter.send_async(request_info, ExtensionCollectionResponse, error_mapping)

	async def post(
		self,
		body: Extension,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Extension:
		"""
		Create new navigation property to extensions for groups
		
		"""
		tags = ['groups.conversationThread']

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
		return await self.request_adapter.send_async(request_info, Extension, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ExtensionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ExtensionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ExtensionsRequest(self.request_adapter, self.path_parameters)

	def by_extension_id(self,
		group_id: str,
		conversationThread_id: str,
		post_id: str,
		extension_id: str,
	) -> ByExtensionIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if conversationThread_id is None:
			raise TypeError("conversationThread_id cannot be null.")
		if post_id is None:
			raise TypeError("post_id cannot be null.")
		if extension_id is None:
			raise TypeError("extension_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["conversationThread%2Did"] =  conversationThread_id
		path_parameters["post%2Did"] =  post_id
		path_parameters["extension%2Did"] =  extension_id

		from .by_extension_id import ByExtensionIdRequest
		return ByExtensionIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

