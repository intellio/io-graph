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
	from .update_request import UpdateRequestRequest
	from .cancel import CancelRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.governance_role_assignment_request import GovernanceRoleAssignmentRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByGovernanceRoleAssignmentRequestIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/governanceResources/{governanceResource%2Did}/roleAssignmentRequests/{governanceRoleAssignmentRequest%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GovernanceRoleAssignmentRequest:
		"""
		Get roleAssignmentRequests from governanceResources
		The collection of role assignment requests for the resource.
		"""
		tags = ['governanceResources.governanceRoleAssignmentRequest']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleAssignmentRequest, error_mapping)

	async def patch(
		self,
		body: GovernanceRoleAssignmentRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GovernanceRoleAssignmentRequest:
		"""
		Update the navigation property roleAssignmentRequests in governanceResources
		
		"""
		tags = ['governanceResources.governanceRoleAssignmentRequest']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleAssignmentRequest, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property roleAssignmentRequests for governanceResources
		
		"""
		tags = ['governanceResources.governanceRoleAssignmentRequest']
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



	def with_url(self, raw_url: str) -> ByGovernanceRoleAssignmentRequestIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGovernanceRoleAssignmentRequestIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGovernanceRoleAssignmentRequestIdRequest(self.request_adapter, self.path_parameters)

	def cancel(self,
		governanceResource_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> CancelRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def update_request(self,
		governanceResource_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> UpdateRequestRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .update_request import UpdateRequestRequest
		return UpdateRequestRequest(self.request_adapter, path_parameters)

	def resource(self,
		governanceResource_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> ResourceRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .resource import ResourceRequest
		return ResourceRequest(self.request_adapter, path_parameters)

	def role_definition(self,
		governanceResource_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> RoleDefinitionRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .role_definition import RoleDefinitionRequest
		return RoleDefinitionRequest(self.request_adapter, path_parameters)

	def subject(self,
		governanceResource_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> SubjectRequest:
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .subject import SubjectRequest
		return SubjectRequest(self.request_adapter, path_parameters)

