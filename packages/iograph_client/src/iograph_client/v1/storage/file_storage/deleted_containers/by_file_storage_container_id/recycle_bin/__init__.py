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
	from .last_modified_by_user import LastModifiedByUserRequest
	from .items import ItemsRequest
	from .created_by_user import CreatedByUserRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.recycle_bin import RecycleBin
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class RecycleBinRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/storage/fileStorage/deletedContainers/{fileStorageContainer%2Did}/recycleBin", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RecycleBin:
		"""
		Get recycleBin from storage
		Recycle bin of the fileStorageContainer. Read-only.
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
		return await self.request_adapter.send_async(request_info, RecycleBin, error_mapping)

	async def patch(
		self,
		body: RecycleBin,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RecycleBin:
		"""
		Update the navigation property recycleBin in storage
		
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
		return await self.request_adapter.send_async(request_info, RecycleBin, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property recycleBin for storage
		
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



	def with_url(self, raw_url: str) -> RecycleBinRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RecycleBinRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RecycleBinRequest(self.request_adapter, self.path_parameters)

	def created_by_user(self,
		fileStorageContainer_id: str,
	) -> CreatedByUserRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .created_by_user import CreatedByUserRequest
		return CreatedByUserRequest(self.request_adapter, path_parameters)

	def items(self,
		fileStorageContainer_id: str,
	) -> ItemsRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .items import ItemsRequest
		return ItemsRequest(self.request_adapter, path_parameters)

	def last_modified_by_user(self,
		fileStorageContainer_id: str,
	) -> LastModifiedByUserRequest:
		if fileStorageContainer_id is None:
			raise TypeError("fileStorageContainer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["fileStorageContainer%2Did"] =  fileStorageContainer_id

		from .last_modified_by_user import LastModifiedByUserRequest
		return LastModifiedByUserRequest(self.request_adapter, path_parameters)

