# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .move_to_catalog import MoveToCatalogRequest
	from .get_applicable_policy_requirements import GetApplicablePolicyRequirementsRequest
	from .incompatible_groups import IncompatibleGroupsRequest
	from .incompatible_access_packages import IncompatibleAccessPackagesRequest
	from .access_packages_incompatible_with_with_uniquename import AccessPackagesIncompatibleWithWithUniqueNameRequest
	from .access_packages_incompatible_with import AccessPackagesIncompatibleWithRequest
	from .access_package_resource_role_scopes import AccessPackageResourceRoleScopesRequest
	from .access_package_catalog import AccessPackageCatalogRequest
	from .access_package_assignment_policies import AccessPackageAssignmentPoliciesRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_package import AccessPackage


class ByAccessPackageIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackage:
		"""
		List accessPackageResourceRoleScopes
		Retrieve an access package with a list of accessPackageResourceRoleScope objects. These objects represent the resource roles that an access package assigns to each subject. Each object links to an accessPackageResourceRole and an accessPackageResourceScope.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackage-list-accesspackageresourcerolescopes?view=graph-rest-beta
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
		Find more info here: https://learn.microsoft.com/graph/api/accesspackage-update?view=graph-rest-beta
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
		Delete an accessPackage object. You can't delete an access package if it has any accessPackageAssignment. To delete the access package, first query if there are any assignments with a filter to indicate the specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'. For more information on how to remove assignments that are still in the delivered state, see Remove an assignment.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackage-delete?view=graph-rest-beta
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



	def with_url(self, raw_url: str) -> ByAccessPackageIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessPackageIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessPackageIdRequest(self.request_adapter, self.path_parameters)

	def access_package_assignment_policies(self,
		accessPackage_id: str,
	) -> AccessPackageAssignmentPoliciesRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .access_package_assignment_policies import AccessPackageAssignmentPoliciesRequest
		return AccessPackageAssignmentPoliciesRequest(self.request_adapter, path_parameters)

	def access_package_catalog(self,
		accessPackage_id: str,
	) -> AccessPackageCatalogRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .access_package_catalog import AccessPackageCatalogRequest
		return AccessPackageCatalogRequest(self.request_adapter, path_parameters)

	def access_package_resource_role_scopes(self,
		accessPackage_id: str,
	) -> AccessPackageResourceRoleScopesRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .access_package_resource_role_scopes import AccessPackageResourceRoleScopesRequest
		return AccessPackageResourceRoleScopesRequest(self.request_adapter, path_parameters)

	def access_packages_incompatible_with(self,
		accessPackage_id: str,
	) -> AccessPackagesIncompatibleWithRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .access_packages_incompatible_with import AccessPackagesIncompatibleWithRequest
		return AccessPackagesIncompatibleWithRequest(self.request_adapter, path_parameters)

	def access_packages_incompatible_with_with_uniquename(self,
		accessPackage_id: str,
		uniqueName: str,
	) -> AccessPackagesIncompatibleWithWithUniqueNameRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if uniqueName is None:
			raise TypeError("uniqueName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["uniqueName"] =  uniqueName

		from .access_packages_incompatible_with_with_uniquename import AccessPackagesIncompatibleWithWithUniqueNameRequest
		return AccessPackagesIncompatibleWithWithUniqueNameRequest(self.request_adapter, path_parameters)

	def incompatible_access_packages(self,
		accessPackage_id: str,
	) -> IncompatibleAccessPackagesRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .incompatible_access_packages import IncompatibleAccessPackagesRequest
		return IncompatibleAccessPackagesRequest(self.request_adapter, path_parameters)

	def incompatible_groups(self,
		accessPackage_id: str,
	) -> IncompatibleGroupsRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .incompatible_groups import IncompatibleGroupsRequest
		return IncompatibleGroupsRequest(self.request_adapter, path_parameters)

	def get_applicable_policy_requirements(self,
		accessPackage_id: str,
	) -> GetApplicablePolicyRequirementsRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .get_applicable_policy_requirements import GetApplicablePolicyRequirementsRequest
		return GetApplicablePolicyRequirementsRequest(self.request_adapter, path_parameters)

	def move_to_catalog(self,
		accessPackage_id: str,
	) -> MoveToCatalogRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id

		from .move_to_catalog import MoveToCatalogRequest
		return MoveToCatalogRequest(self.request_adapter, path_parameters)

