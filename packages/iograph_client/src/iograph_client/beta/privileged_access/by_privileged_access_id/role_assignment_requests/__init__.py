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
	from .count import CountRequest
	from .by_governance_role_assignment_request_id import ByGovernanceRoleAssignmentRequestIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.governance_role_assignment_request import GovernanceRoleAssignmentRequest
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.governance_role_assignment_request_collection_response import GovernanceRoleAssignmentRequestCollectionResponse


class RoleAssignmentRequestsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/privilegedAccess/{privilegedAccess%2Did}/roleAssignmentRequests", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GovernanceRoleAssignmentRequestCollectionResponse:
		"""
		Get roleAssignmentRequests from privilegedAccess
		A collection of role assignment requests for the provider.
		"""
		tags = ['privilegedAccess.governanceRoleAssignmentRequest']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleAssignmentRequestCollectionResponse, error_mapping)

	async def post(
		self,
		body: GovernanceRoleAssignmentRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GovernanceRoleAssignmentRequest:
		"""
		Create new navigation property to roleAssignmentRequests for privilegedAccess
		
		"""
		tags = ['privilegedAccess.governanceRoleAssignmentRequest']

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
		return await self.request_adapter.send_async(request_info, GovernanceRoleAssignmentRequest, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RoleAssignmentRequestsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RoleAssignmentRequestsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RoleAssignmentRequestsRequest(self.request_adapter, self.path_parameters)

	def by_governance_role_assignment_request_id(self,
		privilegedAccess_id: str,
		governanceRoleAssignmentRequest_id: str,
	) -> ByGovernanceRoleAssignmentRequestIdRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")
		if governanceRoleAssignmentRequest_id is None:
			raise TypeError("governanceRoleAssignmentRequest_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id
		path_parameters["governanceRoleAssignmentRequest%2Did"] =  governanceRoleAssignmentRequest_id

		from .by_governance_role_assignment_request_id import ByGovernanceRoleAssignmentRequestIdRequest
		return ByGovernanceRoleAssignmentRequestIdRequest(self.request_adapter, path_parameters)

	def count(self,
		privilegedAccess_id: str,
	) -> CountRequest:
		if privilegedAccess_id is None:
			raise TypeError("privilegedAccess_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["privilegedAccess%2Did"] =  privilegedAccess_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

