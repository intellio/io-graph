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
	from .scoped_role_members import ScopedRoleMembersRequest
	from .restore import RestoreRequest
	from .get_member_objects import GetMemberObjectsRequest
	from .get_member_groups import GetMemberGroupsRequest
	from .check_member_objects import CheckMemberObjectsRequest
	from .check_member_groups import CheckMemberGroupsRequest
	from .members import MembersRequest
	from .extensions import ExtensionsRequest
	from .deleted_members import DeletedMembersRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.administrative_unit import AdministrativeUnit
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByAdministrativeUnitIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/administrativeUnits/{administrativeUnit%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AdministrativeUnit:
		"""
		Get administrativeUnit
		Retrieve the properties and relationships of an administrativeUnit object. Since the administrativeUnit resource supports extensions, you can also use the GET operation to get custom properties and extension data in an administrativeUnit instance.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-get?view=graph-rest-beta
		"""
		tags = ['administrativeUnits.administrativeUnit']

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
		return await self.request_adapter.send_async(request_info, AdministrativeUnit, error_mapping)

	async def patch(
		self,
		body: AdministrativeUnit,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AdministrativeUnit:
		"""
		Update administrativeUnit
		Update the properties of an administrativeUnit object.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-update?view=graph-rest-beta
		"""
		tags = ['administrativeUnits.administrativeUnit']

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
		return await self.request_adapter.send_async(request_info, AdministrativeUnit, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete administrativeUnit
		Delete an administrativeUnit.
		Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-delete?view=graph-rest-beta
		"""
		tags = ['administrativeUnits.administrativeUnit']
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



	def with_url(self, raw_url: str) -> ByAdministrativeUnitIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAdministrativeUnitIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAdministrativeUnitIdRequest(self.request_adapter, self.path_parameters)

	def deleted_members(self,
		administrativeUnit_id: str,
	) -> DeletedMembersRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .deleted_members import DeletedMembersRequest
		return DeletedMembersRequest(self.request_adapter, path_parameters)

	def extensions(self,
		administrativeUnit_id: str,
	) -> ExtensionsRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .extensions import ExtensionsRequest
		return ExtensionsRequest(self.request_adapter, path_parameters)

	def members(self,
		administrativeUnit_id: str,
	) -> MembersRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .members import MembersRequest
		return MembersRequest(self.request_adapter, path_parameters)

	def check_member_groups(self,
		administrativeUnit_id: str,
	) -> CheckMemberGroupsRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .check_member_groups import CheckMemberGroupsRequest
		return CheckMemberGroupsRequest(self.request_adapter, path_parameters)

	def check_member_objects(self,
		administrativeUnit_id: str,
	) -> CheckMemberObjectsRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .check_member_objects import CheckMemberObjectsRequest
		return CheckMemberObjectsRequest(self.request_adapter, path_parameters)

	def get_member_groups(self,
		administrativeUnit_id: str,
	) -> GetMemberGroupsRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .get_member_groups import GetMemberGroupsRequest
		return GetMemberGroupsRequest(self.request_adapter, path_parameters)

	def get_member_objects(self,
		administrativeUnit_id: str,
	) -> GetMemberObjectsRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .get_member_objects import GetMemberObjectsRequest
		return GetMemberObjectsRequest(self.request_adapter, path_parameters)

	def restore(self,
		administrativeUnit_id: str,
	) -> RestoreRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .restore import RestoreRequest
		return RestoreRequest(self.request_adapter, path_parameters)

	def scoped_role_members(self,
		administrativeUnit_id: str,
	) -> ScopedRoleMembersRequest:
		if administrativeUnit_id is None:
			raise TypeError("administrativeUnit_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["administrativeUnit%2Did"] =  administrativeUnit_id

		from .scoped_role_members import ScopedRoleMembersRequest
		return ScopedRoleMembersRequest(self.request_adapter, path_parameters)

