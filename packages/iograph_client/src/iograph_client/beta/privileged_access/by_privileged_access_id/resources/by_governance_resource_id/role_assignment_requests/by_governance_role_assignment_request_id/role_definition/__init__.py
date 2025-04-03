# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .role_setting import RoleSettingRequest
	from .resource import ResourceRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.governance_role_definition import GovernanceRoleDefinition


class RoleDefinitionRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/privilegedAccess/{privilegedAccess%2Did}/resources/{governanceResource%2Did}/roleAssignmentRequests/{governanceRoleAssignmentRequest%2Did}/roleDefinition", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GovernanceRoleDefinition:
		"""
		Get roleDefinition from privilegedAccess
		Read-only. The role definition that the request aims to.
		"""
		tags = ['privilegedAccess.governanceResource']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleDefinition, error_mapping)

	async def patch(
		self,
		body: GovernanceRoleDefinition,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GovernanceRoleDefinition:
		"""
		Update the navigation property roleDefinition in privilegedAccess
		
		"""
		tags = ['privilegedAccess.governanceResource']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleDefinition, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property roleDefinition for privilegedAccess
		
		"""
		tags = ['privilegedAccess.governanceResource']
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



	def with_url(self, raw_url: str) -> RoleDefinitionRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RoleDefinitionRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RoleDefinitionRequest(self.request_adapter, self.path_parameters)

	def resource(self,
		privilegedAccess_id: str,
		governanceResource_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> ResourceRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .resource import ResourceRequest
		return ResourceRequest(self.request_adapter, path_parameters)

	def role_setting(self,
		privilegedAccess_id: str,
		governanceResource_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> RoleSettingRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceResource%2Did"] =  governanceResource_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .role_setting import RoleSettingRequest
		return RoleSettingRequest(self.request_adapter, path_parameters)

