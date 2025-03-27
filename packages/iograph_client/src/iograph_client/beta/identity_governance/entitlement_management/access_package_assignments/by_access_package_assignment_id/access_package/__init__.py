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
	from .move_to_catalog import MoveToCatalogRequest
	from .get_applicable_policy_requirements import GetApplicablePolicyRequirementsRequest
	from .incompatible_groups import IncompatibleGroupsRequest
	from .incompatible_access_packages import IncompatibleAccessPackagesRequest
	from .access_packages_incompatible_with_with_uniquename import AccessPackagesIncompatibleWithWithUniqueNameRequest
	from .access_packages_incompatible_with import AccessPackagesIncompatibleWithRequest
	from .access_package_resource_role_scopes import AccessPackageResourceRoleScopesRequest
	from .access_package_catalog import AccessPackageCatalogRequest
	from .access_package_assignment_policies import AccessPackageAssignmentPoliciesRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.access_package import AccessPackage
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AccessPackageRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments/{accessPackageAssignment%2Did}/accessPackage", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackage:
		"""
		Get accessPackage from identityGovernance
		Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
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
		Update the navigation property accessPackage in identityGovernance
		
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
		Delete navigation property accessPackage for identityGovernance
		
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



	def with_url(self, raw_url: str) -> AccessPackageRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AccessPackageRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AccessPackageRequest(self.request_adapter, self.path_parameters)

	def access_package_assignment_policies(self,
		accessPackageAssignment_id: str,
	) -> AccessPackageAssignmentPoliciesRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .access_package_assignment_policies import AccessPackageAssignmentPoliciesRequest
		return AccessPackageAssignmentPoliciesRequest(self.request_adapter, path_parameters)

	def access_package_catalog(self,
		accessPackageAssignment_id: str,
	) -> AccessPackageCatalogRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .access_package_catalog import AccessPackageCatalogRequest
		return AccessPackageCatalogRequest(self.request_adapter, path_parameters)

	def access_package_resource_role_scopes(self,
		accessPackageAssignment_id: str,
	) -> AccessPackageResourceRoleScopesRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .access_package_resource_role_scopes import AccessPackageResourceRoleScopesRequest
		return AccessPackageResourceRoleScopesRequest(self.request_adapter, path_parameters)

	def access_packages_incompatible_with(self,
		accessPackageAssignment_id: str,
	) -> AccessPackagesIncompatibleWithRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .access_packages_incompatible_with import AccessPackagesIncompatibleWithRequest
		return AccessPackagesIncompatibleWithRequest(self.request_adapter, path_parameters)

	def access_packages_incompatible_with_with_uniquename(self,
		accessPackageAssignment_id: str,
		uniqueName: str,
	) -> AccessPackagesIncompatibleWithWithUniqueNameRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")
		if uniqueName is None:
			raise TypeError("uniqueName cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id
		path_parameters["uniqueName"] =  uniqueName

		from .access_packages_incompatible_with_with_uniquename import AccessPackagesIncompatibleWithWithUniqueNameRequest
		return AccessPackagesIncompatibleWithWithUniqueNameRequest(self.request_adapter, path_parameters)

	def incompatible_access_packages(self,
		accessPackageAssignment_id: str,
	) -> IncompatibleAccessPackagesRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .incompatible_access_packages import IncompatibleAccessPackagesRequest
		return IncompatibleAccessPackagesRequest(self.request_adapter, path_parameters)

	def incompatible_groups(self,
		accessPackageAssignment_id: str,
	) -> IncompatibleGroupsRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .incompatible_groups import IncompatibleGroupsRequest
		return IncompatibleGroupsRequest(self.request_adapter, path_parameters)

	def get_applicable_policy_requirements(self,
		accessPackageAssignment_id: str,
	) -> GetApplicablePolicyRequirementsRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .get_applicable_policy_requirements import GetApplicablePolicyRequirementsRequest
		return GetApplicablePolicyRequirementsRequest(self.request_adapter, path_parameters)

	def move_to_catalog(self,
		accessPackageAssignment_id: str,
	) -> MoveToCatalogRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .move_to_catalog import MoveToCatalogRequest
		return MoveToCatalogRequest(self.request_adapter, path_parameters)

