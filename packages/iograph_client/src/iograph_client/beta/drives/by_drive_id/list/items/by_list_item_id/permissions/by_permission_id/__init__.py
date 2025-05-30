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
	from .revoke_grants import RevokeGrantsRequest
	from .grant import GrantRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.permission import Permission
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByPermissionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/list/items/{listItem%2Did}/permissions/{permission%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> Permission:
		"""
		Get permissions from drives
		The set of permissions for the item. Read-only. Nullable.
		"""
		tags = ['drives.list']

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
		return await self.request_adapter.send_async(request_info, Permission, error_mapping)

	async def patch(
		self,
		body: Permission,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Permission:
		"""
		Update the navigation property permissions in drives
		
		"""
		tags = ['drives.list']

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
		return await self.request_adapter.send_async(request_info, Permission, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property permissions for drives
		
		"""
		tags = ['drives.list']
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



	def with_url(self, raw_url: str) -> ByPermissionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByPermissionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByPermissionIdRequest(self.request_adapter, self.path_parameters)

	def grant(self,
		drive_id: str,
		listItem_id: str,
		permission_id: str,
	) -> GrantRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if permission_id is None:
			raise TypeError("permission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["permission%2Did"] =  permission_id

		from .grant import GrantRequest
		return GrantRequest(self.request_adapter, path_parameters)

	def revoke_grants(self,
		drive_id: str,
		listItem_id: str,
		permission_id: str,
	) -> RevokeGrantsRequest:
		if drive_id is None:
			raise TypeError("drive_id cannot be null.")
		if listItem_id is None:
			raise TypeError("listItem_id cannot be null.")
		if permission_id is None:
			raise TypeError("permission_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["drive%2Did"] =  drive_id
		path_parameters["listItem%2Did"] =  listItem_id
		path_parameters["permission%2Did"] =  permission_id

		from .revoke_grants import RevokeGrantsRequest
		return RevokeGrantsRequest(self.request_adapter, path_parameters)

