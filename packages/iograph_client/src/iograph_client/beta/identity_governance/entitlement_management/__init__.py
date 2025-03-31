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
	from .subjects_with_objectid import SubjectsWithObjectIdRequest
	from .subjects import SubjectsRequest
	from .settings import SettingsRequest
	from .connected_organizations import ConnectedOrganizationsRequest
	from .assignment_requests import AssignmentRequestsRequest
	from .access_packages_with_uniquename import AccessPackagesWithUniqueNameRequest
	from .access_packages import AccessPackagesRequest
	from .access_package_resources import AccessPackageResourcesRequest
	from .access_package_resource_role_scopes import AccessPackageResourceRoleScopesRequest
	from .access_package_resource_requests import AccessPackageResourceRequestsRequest
	from .access_package_resource_environments import AccessPackageResourceEnvironmentsRequest
	from .access_package_catalogs_with_uniquename import AccessPackageCatalogsWithUniqueNameRequest
	from .access_package_catalogs import AccessPackageCatalogsRequest
	from .access_package_assignments import AccessPackageAssignmentsRequest
	from .access_package_assignment_resource_roles import AccessPackageAssignmentResourceRolesRequest
	from .access_package_assignment_requests import AccessPackageAssignmentRequestsRequest
	from .access_package_assignment_policies import AccessPackageAssignmentPoliciesRequest
	from .access_package_assignment_approvals import AccessPackageAssignmentApprovalsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.entitlement_management import EntitlementManagement
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class EntitlementManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EntitlementManagement:
		"""
		Get entitlementManagement from identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, EntitlementManagement, error_mapping)

	async def patch(
		self,
		body: EntitlementManagement,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EntitlementManagement:
		"""
		Update the navigation property entitlementManagement in identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']

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
		return await self.request_adapter.send_async(request_info, EntitlementManagement, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property entitlementManagement for identityGovernance
		
		"""
		tags = ['identityGovernance.entitlementManagement']
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



	def with_url(self, raw_url: str) -> EntitlementManagementRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: EntitlementManagementRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return EntitlementManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_assignment_approvals(self,
	) -> AccessPackageAssignmentApprovalsRequest:
		from .access_package_assignment_approvals import AccessPackageAssignmentApprovalsRequest
		return AccessPackageAssignmentApprovalsRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_assignment_policies(self,
	) -> AccessPackageAssignmentPoliciesRequest:
		from .access_package_assignment_policies import AccessPackageAssignmentPoliciesRequest
		return AccessPackageAssignmentPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_assignment_requests(self,
	) -> AccessPackageAssignmentRequestsRequest:
		from .access_package_assignment_requests import AccessPackageAssignmentRequestsRequest
		return AccessPackageAssignmentRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_assignment_resource_roles(self,
	) -> AccessPackageAssignmentResourceRolesRequest:
		from .access_package_assignment_resource_roles import AccessPackageAssignmentResourceRolesRequest
		return AccessPackageAssignmentResourceRolesRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_assignments(self,
	) -> AccessPackageAssignmentsRequest:
		from .access_package_assignments import AccessPackageAssignmentsRequest
		return AccessPackageAssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_catalogs(self,
	) -> AccessPackageCatalogsRequest:
		from .access_package_catalogs import AccessPackageCatalogsRequest
		return AccessPackageCatalogsRequest(self.request_adapter, self.path_parameters)

	def access_package_catalogs_with_uniquename(self,
		uniqueName: str,
	) -> AccessPackageCatalogsWithUniqueNameRequest:
		if uniqueName is None:
			raise TypeError("uniqueName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["uniqueName"] =  uniqueName

		from .access_package_catalogs_with_uniquename import AccessPackageCatalogsWithUniqueNameRequest
		return AccessPackageCatalogsWithUniqueNameRequest(self.request_adapter, path_parameters)

	@property
	def access_package_resource_environments(self,
	) -> AccessPackageResourceEnvironmentsRequest:
		from .access_package_resource_environments import AccessPackageResourceEnvironmentsRequest
		return AccessPackageResourceEnvironmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_resource_requests(self,
	) -> AccessPackageResourceRequestsRequest:
		from .access_package_resource_requests import AccessPackageResourceRequestsRequest
		return AccessPackageResourceRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_resource_role_scopes(self,
	) -> AccessPackageResourceRoleScopesRequest:
		from .access_package_resource_role_scopes import AccessPackageResourceRoleScopesRequest
		return AccessPackageResourceRoleScopesRequest(self.request_adapter, self.path_parameters)

	@property
	def access_package_resources(self,
	) -> AccessPackageResourcesRequest:
		from .access_package_resources import AccessPackageResourcesRequest
		return AccessPackageResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def access_packages(self,
	) -> AccessPackagesRequest:
		from .access_packages import AccessPackagesRequest
		return AccessPackagesRequest(self.request_adapter, self.path_parameters)

	def access_packages_with_uniquename(self,
		uniqueName: str,
	) -> AccessPackagesWithUniqueNameRequest:
		if uniqueName is None:
			raise TypeError("uniqueName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["uniqueName"] =  uniqueName

		from .access_packages_with_uniquename import AccessPackagesWithUniqueNameRequest
		return AccessPackagesWithUniqueNameRequest(self.request_adapter, path_parameters)

	@property
	def assignment_requests(self,
	) -> AssignmentRequestsRequest:
		from .assignment_requests import AssignmentRequestsRequest
		return AssignmentRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def connected_organizations(self,
	) -> ConnectedOrganizationsRequest:
		from .connected_organizations import ConnectedOrganizationsRequest
		return ConnectedOrganizationsRequest(self.request_adapter, self.path_parameters)

	@property
	def settings(self,
	) -> SettingsRequest:
		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def subjects(self,
	) -> SubjectsRequest:
		from .subjects import SubjectsRequest
		return SubjectsRequest(self.request_adapter, self.path_parameters)

	def subjects_with_objectid(self,
		objectId: str,
	) -> SubjectsWithObjectIdRequest:
		if objectId is None:
			raise TypeError("objectId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["objectId"] =  objectId

		from .subjects_with_objectid import SubjectsWithObjectIdRequest
		return SubjectsWithObjectIdRequest(self.request_adapter, path_parameters)

