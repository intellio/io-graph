# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_contact_folder_id1 import ByContactFolderId1Request
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.contact_folder import ContactFolder
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.contact_folder_collection_response import ContactFolderCollectionResponse


class ChildFoldersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/contactFolders/{contactFolder%2Did}/childFolders", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContactFolderCollectionResponse:
		"""
		Get childFolders from users
		The collection of child folders in the folder. Navigation property. Read-only. Nullable.
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
		Create new navigation property to childFolders for users
		
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


	def with_url(self, raw_url: str) -> ChildFoldersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ChildFoldersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ChildFoldersRequest(self.request_adapter, self.path_parameters)

	def by_contact_folder_id1(self,
		user_id: str,
		contactFolder_id: str,
		contactFolder_id1: str,
	) -> ByContactFolderId1Request:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if contactFolder_id is None:
			raise TypeError("contactFolder_id cannot be null.")
		if contactFolder_id1 is None:
			raise TypeError("contactFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["contactFolder%2Did"] =  contactFolder_id
		path_parameters["contactFolder%2Did1"] =  contactFolder_id1

		from .by_contact_folder_id1 import ByContactFolderId1Request
		return ByContactFolderId1Request(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		contactFolder_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if contactFolder_id is None:
			raise TypeError("contactFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["contactFolder%2Did"] =  contactFolder_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def delta(self,
		user_id: str,
		contactFolder_id: str,
	) -> DeltaRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if contactFolder_id is None:
			raise TypeError("contactFolder_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["contactFolder%2Did"] =  contactFolder_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

