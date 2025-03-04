# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .settings import SettingsRequest
	from .resources import ResourcesRequest
	from .resource_role_scopes import ResourceRoleScopesRequest
	from .resource_requests import ResourceRequestsRequest
	from .resource_environments import ResourceEnvironmentsRequest
	from .connected_organizations import ConnectedOrganizationsRequest
	from .catalogs import CatalogsRequest
	from .assignments import AssignmentsRequest
	from .assignment_requests import AssignmentRequestsRequest
	from .assignment_policies import AssignmentPoliciesRequest
	from .access_packages import AccessPackagesRequest
	from .access_package_assignment_approvals import AccessPackageAssignmentApprovalsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.entitlement_management import EntitlementManagement


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
	def access_packages(self,
	) -> AccessPackagesRequest:
		from .access_packages import AccessPackagesRequest
		return AccessPackagesRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_policies(self,
	) -> AssignmentPoliciesRequest:
		from .assignment_policies import AssignmentPoliciesRequest
		return AssignmentPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_requests(self,
	) -> AssignmentRequestsRequest:
		from .assignment_requests import AssignmentRequestsRequest
		return AssignmentRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def assignments(self,
	) -> AssignmentsRequest:
		from .assignments import AssignmentsRequest
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def catalogs(self,
	) -> CatalogsRequest:
		from .catalogs import CatalogsRequest
		return CatalogsRequest(self.request_adapter, self.path_parameters)

	@property
	def connected_organizations(self,
	) -> ConnectedOrganizationsRequest:
		from .connected_organizations import ConnectedOrganizationsRequest
		return ConnectedOrganizationsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_environments(self,
	) -> ResourceEnvironmentsRequest:
		from .resource_environments import ResourceEnvironmentsRequest
		return ResourceEnvironmentsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_requests(self,
	) -> ResourceRequestsRequest:
		from .resource_requests import ResourceRequestsRequest
		return ResourceRequestsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_role_scopes(self,
	) -> ResourceRoleScopesRequest:
		from .resource_role_scopes import ResourceRoleScopesRequest
		return ResourceRoleScopesRequest(self.request_adapter, self.path_parameters)

	@property
	def resources(self,
	) -> ResourcesRequest:
		from .resources import ResourcesRequest
		return ResourcesRequest(self.request_adapter, self.path_parameters)

	@property
	def settings(self,
	) -> SettingsRequest:
		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, self.path_parameters)

