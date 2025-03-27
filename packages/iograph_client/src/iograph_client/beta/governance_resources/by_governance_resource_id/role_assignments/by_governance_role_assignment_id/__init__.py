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
	from .subject import SubjectRequest
	from .role_definition import RoleDefinitionRequest
	from .resource import ResourceRequest
	from .linked_eligible_role_assignment import LinkedEligibleRoleAssignmentRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.governance_role_assignment import GovernanceRoleAssignment


class ByGovernanceRoleAssignmentIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/governanceResources/{governanceResource%2Did}/roleAssignments/{governanceRoleAssignment%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GovernanceRoleAssignment:
		"""
		Get roleAssignments from governanceResources
		The collection of role assignments for the resource.
		"""
		tags = ['governanceResources.governanceRoleAssignment']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleAssignment, error_mapping)

	async def patch(
		self,
		body: GovernanceRoleAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GovernanceRoleAssignment:
		"""
		Update the navigation property roleAssignments in governanceResources
		
		"""
		tags = ['governanceResources.governanceRoleAssignment']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleAssignment, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property roleAssignments for governanceResources
		
		"""
		tags = ['governanceResources.governanceRoleAssignment']
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



	def with_url(self, raw_url: str) -> ByGovernanceRoleAssignmentIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGovernanceRoleAssignmentIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGovernanceRoleAssignmentIdRequest(self.request_adapter, self.path_parameters)

	def linked_eligible_role_assignment(self,
		governanceResource_id: str,
		governanceRoleAssignment_id: str,
	) -> LinkedEligibleRoleAssignmentRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignment_id is None:
			raise TypeError("governanceRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignment%2Did"] =  governanceRoleAssignment_id

		from .linked_eligible_role_assignment import LinkedEligibleRoleAssignmentRequest
		return LinkedEligibleRoleAssignmentRequest(self.request_adapter, path_parameters)

	def resource(self,
		governanceResource_id: str,
		governanceRoleAssignment_id: str,
	) -> ResourceRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignment_id is None:
			raise TypeError("governanceRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignment%2Did"] =  governanceRoleAssignment_id

		from .resource import ResourceRequest
		return ResourceRequest(self.request_adapter, path_parameters)

	def role_definition(self,
		governanceResource_id: str,
		governanceRoleAssignment_id: str,
	) -> RoleDefinitionRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignment_id is None:
			raise TypeError("governanceRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignment%2Did"] =  governanceRoleAssignment_id

		from .role_definition import RoleDefinitionRequest
		return RoleDefinitionRequest(self.request_adapter, path_parameters)

	def subject(self,
		governanceResource_id: str,
		governanceRoleAssignment_id: str,
	) -> SubjectRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignment_id is None:
			raise TypeError("governanceRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignment%2Did"] =  governanceRoleAssignment_id

		from .subject import SubjectRequest
		return SubjectRequest(self.request_adapter, path_parameters)

