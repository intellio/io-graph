# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
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
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.file_storage_container import FileStorageContainer


class ByFileStorageContainerIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/storage/fileStorage/containers/{fileStorageContainer%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> FileStorageContainer:
		"""
		Get containers from storage
		
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



	@property
	def drive(self,
	) -> DriveRequest:
		from .drive import DriveRequest
		return DriveRequest(self.request_adapter, self.path_parameters)

	@property
	def activate(self,
	) -> ActivateRequest:
		from .activate import ActivateRequest
		return ActivateRequest(self.request_adapter, self.path_parameters)

	@property
	def lock(self,
	) -> LockRequest:
		from .lock import LockRequest
		return LockRequest(self.request_adapter, self.path_parameters)

	@property
	def permanent_delete(self,
	) -> PermanentDeleteRequest:
		from .permanent_delete import PermanentDeleteRequest
		return PermanentDeleteRequest(self.request_adapter, self.path_parameters)

	@property
	def restore(self,
	) -> RestoreRequest:
		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, self.path_parameters)

	@property
	def unlock(self,
	) -> UnlockRequest:
		from .unlock import UnlockRequest
		return UnlockRequest(self.request_adapter, self.path_parameters)

	@property
	def permissions(self,
	) -> PermissionsRequest:
		from .permissions import PermissionsRequest
		return PermissionsRequest(self.request_adapter, self.path_parameters)

	@property
	def recycle_bin(self,
	) -> RecycleBinRequest:
		from .recycle_bin import RecycleBinRequest
		return RecycleBinRequest(self.request_adapter, self.path_parameters)

