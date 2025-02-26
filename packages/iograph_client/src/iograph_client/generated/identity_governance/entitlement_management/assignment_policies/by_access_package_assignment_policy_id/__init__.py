# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .questions import QuestionsRequest
	from .custom_extension_stage_settings import CustomExtensionStageSettingsRequest
	from .catalog import CatalogRequest
	from .access_package import AccessPackageRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.access_package_assignment_policy import AccessPackageAssignmentPolicy


class ByAccessPackageAssignmentPolicyIdRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/assignmentPolicies/{accessPackageAssignmentPolicy%2Did}"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AccessPackageAssignmentPolicy:
		"""
		Get accessPackageAssignmentPolicy
		In Microsoft Entra entitlement management, retrieve the properties and relationships of an
 accessPackageAssignmentPolicy object.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentpolicy-get?view=graph-rest-1.0
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

	async def put(
		self,
		body: AccessPackageAssignmentPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AccessPackageAssignmentPolicy:
		"""
		Update accessPackageAssignmentPolicy
		Update an existing accessPackageAssignmentPolicy object to change one or more of its properties, such as the display name or description.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentpolicy-update?view=graph-rest-1.0
		"""
		tags = ['identityGovernance.entitlementManagement']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PUT,
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
		Delete accessPackageAssignmentPolicy
		In Microsoft Entra entitlement management, delete an accessPackageAssignmentPolicy.
		Find more info here: https://learn.microsoft.com/graph/api/accesspackageassignmentpolicy-delete?view=graph-rest-1.0
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
	def access_package(self,
	) -> AccessPackageRequest:
		from .access_package import AccessPackageRequest
		return AccessPackageRequest(self.request_adapter, self.path_parameters)

	@property
	def catalog(self,
	) -> CatalogRequest:
		from .catalog import CatalogRequest
		return CatalogRequest(self.request_adapter, self.path_parameters)

	@property
	def custom_extension_stage_settings(self,
	) -> CustomExtensionStageSettingsRequest:
		from .custom_extension_stage_settings import CustomExtensionStageSettingsRequest
		return CustomExtensionStageSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def questions(self,
	) -> QuestionsRequest:
		from .questions import QuestionsRequest
		return QuestionsRequest(self.request_adapter, self.path_parameters)

