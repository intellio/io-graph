# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .scoped_members import ScopedMembersRequest
	from .restore import RestoreRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .members import MembersRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.directory_role import DirectoryRole


class ByDirectoryRoleIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/directoryRoles/{directoryRole%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DirectoryRole:
		"""
		Get directoryRole
		Retrieve the properties of a directoryRole object. You can use both the object ID and template ID of the directoryRole with this API. The template ID of a built-in role is immutable and can be seen in the role description on the Microsoft Entra admin center. For details, see Role template IDs.
		Find more info here: https://learn.microsoft.com/graph/api/directoryrole-get?view=graph-rest-beta
		"""
		tags = ['directoryRoles.directoryRole']

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
		return await self.request_adapter.send_async(request_info, DirectoryRole, error_mapping)

	async def patch(
		self,
		body: DirectoryRole,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DirectoryRole:
		"""
		Update entity in directoryRoles
		
		"""
		tags = ['directoryRoles.directoryRole']

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
		return await self.request_adapter.send_async(request_info, DirectoryRole, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete entity from directoryRoles
		
		"""
		tags = ['directoryRoles.directoryRole']
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



	def with_url(self, raw_url: str) -> ByDirectoryRoleIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByDirectoryRoleIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByDirectoryRoleIdRequest(self.request_adapter, self.path_parameters)

	def members(self,
		directoryRole_id: str,
	) -> MembersRequest:
		if directoryRole_id is None:
			raise TypeError("directoryRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRole%2Did"] =  directoryRole_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		directoryRole_id: str,
	) -> CheckMemberGroupsRequest:
		if directoryRole_id is None:
			raise TypeError("directoryRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRole%2Did"] =  directoryRole_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		directoryRole_id: str,
	) -> CheckMemberObjectsRequest:
		if directoryRole_id is None:
			raise TypeError("directoryRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRole%2Did"] =  directoryRole_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		directoryRole_id: str,
	) -> GetMemberGroupsRequest:
		if directoryRole_id is None:
			raise TypeError("directoryRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRole%2Did"] =  directoryRole_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		directoryRole_id: str,
	) -> GetMemberObjectsRequest:
		if directoryRole_id is None:
			raise TypeError("directoryRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRole%2Did"] =  directoryRole_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def restore(self,
		directoryRole_id: str,
	) -> RestoreRequest:
		if directoryRole_id is None:
			raise TypeError("directoryRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRole%2Did"] =  directoryRole_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def scoped_members(self,
		directoryRole_id: str,
	) -> ScopedMembersRequest:
		if directoryRole_id is None:
			raise TypeError("directoryRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["directoryRole%2Did"] =  directoryRole_id

		from .scoped_members import ScopedMembersRequest
		return ScopedMembersRequest(self.request_adapter, path_parameters)

