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
	from .my import MyRequest
	from .count import CountRequest
	from .by_access_package_assignment_resource_role_id import ByAccessPackageAssignmentResourceRoleIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.access_package_assignment_resource_role import AccessPackageAssignmentResourceRole
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_package_assignment_resource_role_collection_response import AccessPackageAssignmentResourceRoleCollectionResponse


class AccessPackageAssignmentResourceRolesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments/{accessPackageAssignment%2Did}/accessPackageAssignmentResourceRoles", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageAssignmentResourceRoleCollectionResponse:
		"""
		Get accessPackageAssignmentResourceRoles from identityGovernance
		The resource roles delivered to the target user for this assignment. Read-only. Nullable.
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignmentResourceRoleCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessPackageAssignmentResourceRole,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageAssignmentResourceRole:
		"""
		Create new navigation property to accessPackageAssignmentResourceRoles for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignmentResourceRole, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AccessPackageAssignmentResourceRolesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AccessPackageAssignmentResourceRolesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AccessPackageAssignmentResourceRolesRequest(self.request_adapter, self.path_parameters)

	def by_access_package_assignment_resource_role_id(self,
		accessPackageAssignment_id: str,
		accessPackageAssignmentResourceRole_id: str,
	) -> ByAccessPackageAssignmentResourceRoleIdRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")
		if accessPackageAssignmentResourceRole_id is None:
			raise TypeError("accessPackageAssignmentResourceRole_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id
		path_parameters["accessPackageAssignmentResourceRole%2Did"] =  accessPackageAssignmentResourceRole_id

		from .by_access_package_assignment_resource_role_id import ByAccessPackageAssignmentResourceRoleIdRequest
		return ByAccessPackageAssignmentResourceRoleIdRequest(self.request_adapter, path_parameters)

	def count(self,
		accessPackageAssignment_id: str,
	) -> CountRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def my(self,
		accessPackageAssignment_id: str,
	) -> MyRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .my import MyRequest
		return MyRequest(self.request_adapter, path_parameters)

