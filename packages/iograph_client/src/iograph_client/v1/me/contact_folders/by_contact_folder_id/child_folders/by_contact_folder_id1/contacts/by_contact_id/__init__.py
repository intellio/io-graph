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
	from .photo import PhotoRequest
	from .extensions import ExtensionsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.v1.contact import Contact
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByContactIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/contactFolders/{contactFolder%2Did}/childFolders/{contactFolder%2Did1}/contacts/{contact%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Contact:
		"""
		Get contacts from me
		The contacts in the folder. Navigation property. Read-only. Nullable.
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
		return await self.request_adapter.send_async(request_info, Contact, error_mapping)

	async def patch(
		self,
		body: Contact,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Contact:
		"""
		Update the navigation property contacts in me
		
		"""
		tags = ['me.contactFolder']

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
		return await self.request_adapter.send_async(request_info, Contact, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property contacts for me
		
		"""
		tags = ['me.contactFolder']
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



	def with_url(self, raw_url: str) -> ByContactIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByContactIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByContactIdRequest(self.request_adapter, self.path_parameters)

	def extensions(self,
		contactFolder_id: str,
		contactFolder_id1: str,
		contact_id: str,
	) -> ExtensionsRequest:
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

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def photo(self,
		contactFolder_id: str,
		contactFolder_id1: str,
		contact_id: str,
	) -> PhotoRequest:
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

		from .photo import PhotoRequest
		return PhotoRequest(self.request_adapter, path_parameters)

