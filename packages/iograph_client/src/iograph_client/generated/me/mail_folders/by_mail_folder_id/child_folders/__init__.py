# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_mail_folder_id1 import ByMailFolderId1Request
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.mail_folder import MailFolder
from iograph_models.models.mail_folder_collection_response import MailFolderCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ChildFoldersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/mailFolders/{mailFolder%2Did}/childFolders", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MailFolderCollectionResponse:
		"""
		List childFolders
		Get the folder collection under the specified folder. You can use the .../me/mailFolders shortcut to get the top-level
folder collection and navigate to another folder. By default, this operation does not return hidden folders. Use a query parameter includeHiddenFolders to include them in the response.
		Find more info here: https://learn.microsoft.com/graph/api/mailfolder-list-childfolders?view=graph-rest-1.0
		"""
		tags = ['me.mailFolder']

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
		return await self.request_adapter.send_async(request_info, MailFolderCollectionResponse, error_mapping)

	async def post(
		self,
		body: MailFolder,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MailFolder:
		"""
		Create child folder
		Use this API to create a new child mailFolder. If you intend a new folder to be hidden, you must set the isHidden property to true on creation.
		Find more info here: https://learn.microsoft.com/graph/api/mailfolder-post-childfolders?view=graph-rest-1.0
		"""
		tags = ['me.mailFolder']

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
		return await self.request_adapter.send_async(request_info, MailFolder, error_mapping)

	class GetQueryParams(BaseModel):
		includeHiddenFolders: str = Field(default=None,serialization_alias="includeHiddenFolders")
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

	def by_mail_folder_id1(self,
		mailFolder_id: str,
		mailFolder_id1: str,
	) -> ByMailFolderId1Request:
		if mailFolder_id is None:
			raise TypeError("mailFolder_id cannot be null.")
		if mailFolder_id1 is None:
			raise TypeError("mailFolder_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["mailFolder%2Did"] =  mailFolder_id
		path_parameters["mailFolder%2Did1"] =  mailFolder_id1

		from .by_mail_folder_id1 import ByMailFolderId1Request
		return ByMailFolderId1Request(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

