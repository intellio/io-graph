# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .questions import QuestionsRequest
	from .custom_extension_stage_settings import CustomExtensionStageSettingsRequest
	from .catalog import CatalogRequest
	from .access_package import AccessPackageRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.v1.access_package_assignment_policy import AccessPackageAssignmentPolicy
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByAccessPackageAssignmentPolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}/assignmentPolicies/{accessPackageAssignmentPolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageAssignmentPolicy:
		"""
		Get assignmentPolicies from identityGovernance
		Read-only. Nullable. Supports $expand.
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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicy, error_mapping)

	async def patch(
		self,
		body: AccessPackageAssignmentPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageAssignmentPolicy:
		"""
		Update the navigation property assignmentPolicies in identityGovernance
		
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
		return await self.request_adapter.send_async(request_info, AccessPackageAssignmentPolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property assignmentPolicies for identityGovernance
		
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



	def with_url(self, raw_url: str) -> ByAccessPackageAssignmentPolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByAccessPackageAssignmentPolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByAccessPackageAssignmentPolicyIdRequest(self.request_adapter, self.path_parameters)

	def access_package(self,
		accessPackage_id: str,
		accessPackageAssignmentPolicy_id: str,
	) -> AccessPackageRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id

		from .access_package import AccessPackageRequest
		return AccessPackageRequest(self.request_adapter, path_parameters)

	def catalog(self,
		accessPackage_id: str,
		accessPackageAssignmentPolicy_id: str,
	) -> CatalogRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id

		from .catalog import CatalogRequest
		return CatalogRequest(self.request_adapter, path_parameters)

	def custom_extension_stage_settings(self,
		accessPackage_id: str,
		accessPackageAssignmentPolicy_id: str,
	) -> CustomExtensionStageSettingsRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id

		from .custom_extension_stage_settings import CustomExtensionStageSettingsRequest
		return CustomExtensionStageSettingsRequest(self.request_adapter, path_parameters)

	def questions(self,
		accessPackage_id: str,
		accessPackageAssignmentPolicy_id: str,
	) -> QuestionsRequest:
		if accessPackage_id is None:
			raise TypeError("accessPackage_id cannot be null.")
		if accessPackageAssignmentPolicy_id is None:
			raise TypeError("accessPackageAssignmentPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["accessPackage%2Did"] =  accessPackage_id
		path_parameters["accessPackageAssignmentPolicy%2Did"] =  accessPackageAssignmentPolicy_id

		from .questions import QuestionsRequest
		return QuestionsRequest(self.request_adapter, path_parameters)

