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
	from .by_file_storage_container_id import ByFileStorageContainerIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.file_storage_container import FileStorageContainer
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.file_storage_container_collection_response import FileStorageContainerCollectionResponse


class ContainersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/storage/fileStorage/containers", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> FileStorageContainerCollectionResponse:
		"""
		List containers
		Retrieve a list of fileStorageContainer objects that are visible to the caller. The containerTypeId filter parameter is required.
		Find more info here: https://learn.microsoft.com/graph/api/filestorage-list-containers?view=graph-rest-1.0
		"""
		tags = ['storage.fileStorage']

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
		return await self.request_adapter.send_async(request_info, FileStorageContainerCollectionResponse, error_mapping)

	async def post(
		self,
		body: FileStorageContainer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> FileStorageContainer:
		"""
		Create fileStorageContainer
		Create a new fileStorageContainer object.  The container type identified by containerTypeId must be registered in the tenant.  For delegated calls, the calling user is set as the owner of the fileStorageContainer. 
		Find more info here: https://learn.microsoft.com/graph/api/filestoragecontainer-post?view=graph-rest-1.0
		"""
		tags = ['storage.fileStorage']

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
		return await self.request_adapter.send_async(request_info, FileStorageContainer, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ContainersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ContainersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ContainersRequest(self.request_adapter, self.path_parameters)

	def by_file_storage_container_id(self,
		fileStorageContainer_id: str,
	) -> ByFileStorageContainerIdRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .by_file_storage_container_id import ByFileStorageContainerIdRequest
		return ByFileStorageContainerIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

