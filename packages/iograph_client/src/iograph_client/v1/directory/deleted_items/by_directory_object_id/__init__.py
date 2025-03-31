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
	from .graph_user import GraphUserRequest
	from .graph_service_principal import GraphServicePrincipalRequest
	from .restore import RestoreRequest
	from .graph_group import GraphGroupRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .graph_device import GraphDeviceRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .graph_application import GraphApplicationRequest
	from .graph_administrative_unit import GraphAdministrativeUnitRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.directory_object import DirectoryObject
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByDirectoryObjectIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directory/deletedItems/{directoryObject%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryObject:
		"""
		Get deleted item (directory object)
		Retrieve the properties of a recently deleted application, group, servicePrincipal, administrative unit, or user object from deleted items.
		Find more info here: https://learn.microsoft.com/graph/api/directory-deleteditems-get?view=graph-rest-1.0
		"""
		tags = ['directory.directoryObject']

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
		return await self.request_adapter.send_async(request_info, DirectoryObject, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Permanently delete an item (directory object)
		Permanently delete a recently deleted application, group, servicePrincipal, or user object from deleted items. After an item is permanently deleted, it cannot be restored. Administrative units cannot be permanently deleted by using the deletedItems API. Soft-deleted administrative units will be permanently deleted 30 days after initial deletion unless they are restored.
		Find more info here: https://learn.microsoft.com/graph/api/directory-deleteditems-delete?view=graph-rest-1.0
		"""
		tags = ['directory.directoryObject']
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


	def with_url(self, raw_url: str) -> ByDirectoryObjectIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDirectoryObjectIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDirectoryObjectIdRequest(self.request_adapter, self.path_parameters)

	def graph_administrative_unit(self,
		directoryObject_id: str,
	) -> GraphAdministrativeUnitRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_administrative_unit import GraphAdministrativeUnitRequest
		return GraphAdministrativeUnitRequest(self.request_adapter, path_parameters)

	def graph_application(self,
		directoryObject_id: str,
	) -> GraphApplicationRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_application import GraphApplicationRequest
		return GraphApplicationRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		directoryObject_id: str,
	) -> CheckMemberGroupsRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		directoryObject_id: str,
	) -> CheckMemberObjectsRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def graph_device(self,
		directoryObject_id: str,
	) -> GraphDeviceRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_device import GraphDeviceRequest
		return GraphDeviceRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		directoryObject_id: str,
	) -> GetMemberGroupsRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		directoryObject_id: str,
	) -> GetMemberObjectsRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def graph_group(self,
		directoryObject_id: str,
	) -> GraphGroupRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_group import GraphGroupRequest
		return GraphGroupRequest(self.request_adapter, path_parameters)

	def restore(self,
		directoryObject_id: str,
	) -> RestoreRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def graph_service_principal(self,
		directoryObject_id: str,
	) -> GraphServicePrincipalRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_service_principal import GraphServicePrincipalRequest
		return GraphServicePrincipalRequest(self.request_adapter, path_parameters)

	def graph_user(self,
		directoryObject_id: str,
	) -> GraphUserRequest:
		if directoryObject_id is None:
			raise TypeError("directoryObject_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryObject%2Did"] =  directoryObject_id

		from .graph_user import GraphUserRequest
		return GraphUserRequest(self.request_adapter, path_parameters)

