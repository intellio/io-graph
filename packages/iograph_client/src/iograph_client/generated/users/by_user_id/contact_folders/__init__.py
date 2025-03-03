# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_contact_folder_id import ByContactFolderIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.contact_folder_collection_response import ContactFolderCollectionResponse
from iograph_models.models.contact_folder import ContactFolder
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ContactFoldersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/contactFolders", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContactFolderCollectionResponse:
		"""
		Get contactFolders from users
		The user's contacts folders. Read-only. Nullable.
		"""
		tags = ['users.contactFolder']

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
		return await self.request_adapter.send_async(request_info, ContactFolderCollectionResponse, error_mapping)

	async def post(
		self,
		body: ContactFolder,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContactFolder:
		"""
		Create new navigation property to contactFolders for users
		
		"""
		tags = ['users.contactFolder']

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
		return await self.request_adapter.send_async(request_info, ContactFolder, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ContactFoldersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ContactFoldersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ContactFoldersRequest(self.request_adapter, self.path_parameters)

	def by_contact_folder_id(self,
		user_id: str,
		contactFolder_id: str,
	) -> ByContactFolderIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if contactFolder_id is None:
			raise TypeError("contactFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["contactFolder%2Did"] =  contactFolder_id

		from .by_contact_folder_id import ByContactFolderIdRequest
		return ByContactFolderIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

