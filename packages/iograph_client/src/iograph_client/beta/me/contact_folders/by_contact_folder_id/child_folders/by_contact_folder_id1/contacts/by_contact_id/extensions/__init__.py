# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_extension_id import ByExtensionIdRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.beta.extension_collection_response import ExtensionCollectionResponse
from iograph_models.beta.extension import Extension
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ExtensionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/contactFolders/{contactFolder%2Did}/childFolders/{contactFolder%2Did1}/contacts/{contact%2Did}/extensions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ExtensionCollectionResponse:
		"""
		Get extensions from me
		The collection of open extensions defined for the contact. Nullable.
		"""
		tags = ['me.contactFolder']

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
		Create new navigation property to extensions for me
		
		"""
		tags = ['me.contactFolder']

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
		contactFolder_id: str,
		contactFolder_id1: str,
		contact_id: str,
		extension_id: str,
	) -> ByExtensionIdRequest:
		if contactFolder_id is None:
			raise TypeError("contactFolder_id cannot be null.")
		if contactFolder_id1 is None:
			raise TypeError("contactFolder_id1 cannot be null.")
		if contact_id is None:
			raise TypeError("contact_id cannot be null.")
		if extension_id is None:
			raise TypeError("extension_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contactFolder%2Did"] =  contactFolder_id
		path_parameters["contactFolder%2Did1"] =  contactFolder_id1
		path_parameters["contact%2Did"] =  contact_id
		path_parameters["extension%2Did"] =  extension_id

		from .by_extension_id import ByExtensionIdRequest
		return ByExtensionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		contactFolder_id: str,
		contactFolder_id1: str,
		contact_id: str,
	) -> CountRequest:
		if contactFolder_id is None:
			raise TypeError("contactFolder_id cannot be null.")
		if contactFolder_id1 is None:
			raise TypeError("contactFolder_id1 cannot be null.")
		if contact_id is None:
			raise TypeError("contact_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contactFolder%2Did"] =  contactFolder_id
		path_parameters["contactFolder%2Did1"] =  contactFolder_id1
		path_parameters["contact%2Did"] =  contact_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

