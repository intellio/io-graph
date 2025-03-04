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
	from .count import CountRequest
	from .by_permission_id import ByPermissionIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.permission import Permission
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.permission_collection_response import PermissionCollectionResponse


class PermissionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/storage/fileStorage/containers/{fileStorageContainer%2Did}/permissions", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PermissionCollectionResponse:
		"""
		Get permissions from storage
		The set of permissions for users in the fileStorageContainer. Permission for each user is set by the roles property. The possible values are: reader, writer, manager, and owner. Read-write.
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
		return await self.request_adapter.send_async(request_info, PermissionCollectionResponse, error_mapping)

	async def post(
		self,
		body: Permission,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Permission:
		"""
		Create new navigation property to permissions for storage
		
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
		return await self.request_adapter.send_async(request_info, Permission, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> PermissionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: PermissionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return PermissionsRequest(self.request_adapter, self.path_parameters)

	def by_permission_id(self,
		fileStorageContainer_id: str,
		permission_id: str,
	) -> ByPermissionIdRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")
		if permission_id is None:
			raise TypeError("permission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id
		path_parameters["permission%2Did"] =  permission_id

		from .by_permission_id import ByPermissionIdRequest
		return ByPermissionIdRequest(self.request_adapter, path_parameters)

	def count(self,
		fileStorageContainer_id: str,
	) -> CountRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

