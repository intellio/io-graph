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
	from .recycle_bin import RecycleBinRequest
	from .permissions import PermissionsRequest
	from .unlock import UnlockRequest
	from .restore import RestoreRequest
	from .permanent_delete import PermanentDeleteRequest
	from .lock import LockRequest
	from .activate import ActivateRequest
	from .drive import DriveRequest
	from .columns import ColumnsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.file_storage_container import FileStorageContainer


class ByFileStorageContainerIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/storage/fileStorage/containers/{fileStorageContainer%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> FileStorageContainer:
		"""
		Get fileStorageContainer
		Retrieve the properties of a fileStorageContainer.
		Find more info here: https://learn.microsoft.com/graph/api/filestoragecontainer-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, FileStorageContainer, error_mapping)

	async def patch(
		self,
		body: FileStorageContainer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> FileStorageContainer:
		"""
		Update the navigation property containers in storage
		
		"""
		tags = ['storage.fileStorage']

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
		return await self.request_adapter.send_async(request_info, FileStorageContainer, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property containers for storage
		
		"""
		tags = ['storage.fileStorage']
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



	def with_url(self, raw_url: str) -> ByFileStorageContainerIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByFileStorageContainerIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByFileStorageContainerIdRequest(self.request_adapter, self.path_parameters)

	def columns(self,
		fileStorageContainer_id: str,
	) -> ColumnsRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .columns import ColumnsRequest
		return ColumnsRequest(self.request_adapter, path_parameters)

	def drive(self,
		fileStorageContainer_id: str,
	) -> DriveRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, path_parameters)

	def activate(self,
		fileStorageContainer_id: str,
	) -> ActivateRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .activate import ActivateRequest
		return ActivateRequest(self.request_adapter, path_parameters)

	def lock(self,
		fileStorageContainer_id: str,
	) -> LockRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .lock import LockRequest
		return LockRequest(self.request_adapter, path_parameters)

	def permanent_delete(self,
		fileStorageContainer_id: str,
	) -> PermanentDeleteRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, path_parameters)

	def restore(self,
		fileStorageContainer_id: str,
	) -> RestoreRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def unlock(self,
		fileStorageContainer_id: str,
	) -> UnlockRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .unlock import UnlockRequest
		return UnlockRequest(self.request_adapter, path_parameters)

	def permissions(self,
		fileStorageContainer_id: str,
	) -> PermissionsRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .permissions import PermissionsRequest
		return PermissionsRequest(self.request_adapter, path_parameters)

	def recycle_bin(self,
		fileStorageContainer_id: str,
	) -> RecycleBinRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .recycle_bin import RecycleBinRequest
		return RecycleBinRequest(self.request_adapter, path_parameters)

