# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .resource_role_scopes import ResourceRoleScopesRequest
	from .get_applicable_policy_requirements import GetApplicablePolicyRequirementsRequest
	from .incompatible_groups import IncompatibleGroupsRequest
	from .incompatible_access_packages import IncompatibleAccessPackagesRequest
	from .catalog import CatalogRequest
	from .assignment_policies import AssignmentPoliciesRequest
	from .access_packages_incompatible_with import AccessPackagesIncompatibleWithRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.access_package import AccessPackage


class ByAccessPackageIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackage:
		"""
		Get accessPackage
		Retrieve the properties and relationships of an accessPackage object.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackage-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)

	async def patch(
		self,
		body: AccessPackage,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackage:
		"""
		Update accessPackage
		Update an existing accessPackage object to change one or more of its properties, such as the display name or description.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackage-update?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, AccessPackage, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete accessPackage
		Delete an accessPackage object. You cannot delete an access package if it has any accessPackageAssignment.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackage-delete?view=graph-rest-1.0
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



	@property
	def access_packages_incompatible_with(self,
	) -> AccessPackagesIncompatibleWithRequest:
		from .access_packages_incompatible_with import AccessPackagesIncompatibleWithRequest
		return AccessPackagesIncompatibleWithRequest(self.request_adapter, self.path_parameters)

	@property
	def assignment_policies(self,
	) -> AssignmentPoliciesRequest:
		from .assignment_policies import AssignmentPoliciesRequest
		return AssignmentPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def catalog(self,
	) -> CatalogRequest:
		from .catalog import CatalogRequest
		return CatalogRequest(self.request_adapter, self.path_parameters)

	@property
	def incompatible_access_packages(self,
	) -> IncompatibleAccessPackagesRequest:
		from .incompatible_access_packages import IncompatibleAccessPackagesRequest
		return IncompatibleAccessPackagesRequest(self.request_adapter, self.path_parameters)

	@property
	def incompatible_groups(self,
	) -> IncompatibleGroupsRequest:
		from .incompatible_groups import IncompatibleGroupsRequest
		return IncompatibleGroupsRequest(self.request_adapter, self.path_parameters)

	@property
	def get_applicable_policy_requirements(self,
	) -> GetApplicablePolicyRequirementsRequest:
		from .get_applicable_policy_requirements import GetApplicablePolicyRequirementsRequest
		return GetApplicablePolicyRequirementsRequest(self.request_adapter, self.path_parameters)

	@property
	def resource_role_scopes(self,
	) -> ResourceRoleScopesRequest:
		from .resource_role_scopes import ResourceRoleScopesRequest
		return ResourceRoleScopesRequest(self.request_adapter, self.path_parameters)

