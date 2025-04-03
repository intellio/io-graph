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
	from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
	from .additional_access_with_accesspackageid_incompatibleaccesspackageid import AdditionalAccessWithAccessPackageIdIncompatibleAccessPackageIdRequest
	from .additional_access import AdditionalAccessRequest
	from .count import CountRequest
	from .by_access_package_assignment_id import ByAccessPackageAssignmentIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.access_package_assignment_collection_response import AccessPackageAssignmentCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.access_package_assignment import AccessPackageAssignment


class AccessPackageAssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackageAssignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageAssignmentCollectionResponse:
		"""
		List accessPackageAssignments
		Retrieve a list of accessPackageAssignment objects in Microsoft Entra entitlement management. For directory-wide administrators, the resulting list includes all the assignments, current and well as expired, that the caller has access to read, across all catalogs and access packages.  If the caller is on behalf of a delegated user who is assigned only to catalog-specific delegated administrative roles, the request must supply a filter to indicate a specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'.
		Find more info here: https://learn.microsoft.com/graph/api/entitlementmanagement-list-accesspackageassignments?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: AccessPackageAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageAssignment:
		"""
		Create new navigation property to accessPackageAssignments for identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AccessPackageAssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AccessPackageAssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AccessPackageAssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_access_package_assignment_id(self,
		accessPackageAssignment_id: str,
	) -> ByAccessPackageAssignmentIdRequest:
		if accessPackageAssignment_id is None:
			raise TypeError("accessPackageAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageAssignment%2Did"] =  accessPackageAssignment_id

		from .by_access_package_assignment_id import ByAccessPackageAssignmentIdRequest
		return ByAccessPackageAssignmentIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def additional_access(self,
	) -> AdditionalAccessRequest:
		from .additional_access import AdditionalAccessRequest
		return AdditionalAccessRequest(self.request_adapter, self.path_parameters)

	def additional_access_with_accesspackageid_incompatibleaccesspackageid(self,
		accessPackageId: str,
		incompatibleAccessPackageId: str,
	) -> AdditionalAccessWithAccessPackageIdIncompatibleAccessPackageIdRequest:
		if accessPackageId is None:
			raise TypeError("accessPackageId cannot be null.")
		if incompatibleAccessPackageId is None:
			raise TypeError("incompatibleAccessPackageId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackageId"] =  accessPackageId
		path_parameters["incompatibleAccessPackageId"] =  incompatibleAccessPackageId

		from .additional_access_with_accesspackageid_incompatibleaccesspackageid import AdditionalAccessWithAccessPackageIdIncompatibleAccessPackageIdRequest
		return AdditionalAccessWithAccessPackageIdIncompatibleAccessPackageIdRequest(self.request_adapter, path_parameters)

	def filter_by_current_user_with_on(self,
		on: str,
	) -> FilterByCurrentUserWithOnRequest:
		if on is None:
			raise TypeError("on cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["on"] =  on

		from .filter_by_current_user_with_on import FilterByCurrentUserWithOnRequest
		return FilterByCurrentUserWithOnRequest(self.request_adapter, path_parameters)

