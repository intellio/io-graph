# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_contact_folder_id1 import ByContactFolderId1Request
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.contact_folder_collection_response import ContactFolderCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.contact_folder import ContactFolder


class ChildFoldersRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/me/contactFolders/{contactFolder%2Did}/childFolders"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> ContactFolderCollectionResponse:
		"""
		List childFolders
		Get a collection of child folders under the specified contact folder.
		Find more info here: https://learn.microsoft.com/graph/api/contactfolder-list-childfolders?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, ContactFolderCollectionResponse, error_mapping)

	async def post(
		self,
		body: ContactFolder,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ContactFolder:
		"""
		Create ContactFolder
		Create a new contactFolder as a child of a specified folder.  You can also create a new contactFolder under the user's default contact folder.
		Find more info here: https://learn.microsoft.com/graph/api/contactfolder-post-childfolders?view=graph-rest-1.0
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


	def by_contact_folder_id1(self,
		contactFolder_id: str,
		contactFolder_id1: str,
	) -> ByContactFolderId1Request:
		if contactFolder_id is None:
			raise TypeError("contactFolder_id cannot be null.")
		if contactFolder_id1 is None:
			raise TypeError("contactFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["contactFolder%2Did"] =  contactFolder_id
		path_parameters["contactFolder%2Did1"] =  contactFolder_id1

		from .by_contact_folder_id1 import ByContactFolderId1Request
		return ByContactFolderId1Request(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

