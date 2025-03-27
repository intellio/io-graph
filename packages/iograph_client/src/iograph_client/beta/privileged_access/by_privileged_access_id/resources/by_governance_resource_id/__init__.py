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
	from .role_settings import RoleSettingsRequest
	from .role_definitions import RoleDefinitionsRequest
	from .role_assignments import RoleAssignmentsRequest
	from .role_assignment_requests import RoleAssignmentRequestsRequest
	from .parent import ParentRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.governance_resource import GovernanceResource
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByGovernanceResourceIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/privilegedAccess/{privilegedAccess%2Did}/resources/{governanceResource%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GovernanceResource:
		"""
		Get resources from privilegedAccess
		A collection of resources for the provider.
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
		return await self.request_adapter.send_async(request_info, GovernanceResource, error_mapping)

	async def patch(
		self,
		body: GovernanceResource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GovernanceResource:
		"""
		Update the navigation property resources in privilegedAccess
		
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
		return await self.request_adapter.send_async(request_info, GovernanceResource, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property resources for privilegedAccess
		
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



	def with_url(self, raw_url: str) -> ByGovernanceResourceIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGovernanceResourceIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGovernanceResourceIdRequest(self.request_adapter, self.path_parameters)

	def parent(self,
		privilegedAccess_id: str,
		governanceResource_id: str,
	) -> ParentRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceResource%2Did"] =  governanceResource_id

		from .parent import ParentRequest
		return ParentRequest(self.request_adapter, path_parameters)

	def role_assignment_requests(self,
		privilegedAccess_id: str,
		governanceResource_id: str,
	) -> RoleAssignmentRequestsRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceResource%2Did"] =  governanceResource_id

		from .role_assignment_requests import RoleAssignmentRequestsRequest
		return RoleAssignmentRequestsRequest(self.request_adapter, path_parameters)

	def role_assignments(self,
		privilegedAccess_id: str,
		governanceResource_id: str,
	) -> RoleAssignmentsRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceResource%2Did"] =  governanceResource_id

		from .role_assignments import RoleAssignmentsRequest
		return RoleAssignmentsRequest(self.request_adapter, path_parameters)

	def role_definitions(self,
		privilegedAccess_id: str,
		governanceResource_id: str,
	) -> RoleDefinitionsRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceResource%2Did"] =  governanceResource_id

		from .role_definitions import RoleDefinitionsRequest
		return RoleDefinitionsRequest(self.request_adapter, path_parameters)

	def role_settings(self,
		privilegedAccess_id: str,
		governanceResource_id: str,
	) -> RoleSettingsRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceResource_id is None:
			raise TypeError("governanceResource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceResource%2Did"] =  governanceResource_id

		from .role_settings import RoleSettingsRequest
		return RoleSettingsRequest(self.request_adapter, path_parameters)

