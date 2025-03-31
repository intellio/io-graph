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
	from .count import CountRequest
	from .by_role_scope_tag_auto_assignment_id import ByRoleScopeTagAutoAssignmentIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.role_scope_tag_auto_assignment import RoleScopeTagAutoAssignment
from iograph_models.beta.role_scope_tag_auto_assignment_collection_response import RoleScopeTagAutoAssignmentCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class AssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/roleScopeTags/{roleScopeTag%2Did}/assignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> RoleScopeTagAutoAssignmentCollectionResponse:
		"""
		Get assignments from deviceManagement
		The list of assignments for this Role Scope Tag.
		"""
		tags = ['deviceManagement.roleScopeTag']

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
		return await self.request_adapter.send_async(request_info, RoleScopeTagAutoAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: RoleScopeTagAutoAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RoleScopeTagAutoAssignment:
		"""
		Create new navigation property to assignments for deviceManagement
		
		"""
		tags = ['deviceManagement.roleScopeTag']

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
		return await self.request_adapter.send_async(request_info, RoleScopeTagAutoAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_role_scope_tag_auto_assignment_id(self,
		roleScopeTag_id: str,
		roleScopeTagAutoAssignment_id: str,
	) -> ByRoleScopeTagAutoAssignmentIdRequest:
		if roleScopeTag_id is None:
			raise TypeError("roleScopeTag_id cannot be null.")
		if roleScopeTagAutoAssignment_id is None:
			raise TypeError("roleScopeTagAutoAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["roleScopeTag%2Did"] =  roleScopeTag_id
		path_parameters["roleScopeTagAutoAssignment%2Did"] =  roleScopeTagAutoAssignment_id

		from .by_role_scope_tag_auto_assignment_id import ByRoleScopeTagAutoAssignmentIdRequest
		return ByRoleScopeTagAutoAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		roleScopeTag_id: str,
	) -> CountRequest:
		if roleScopeTag_id is None:
			raise TypeError("roleScopeTag_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["roleScopeTag%2Did"] =  roleScopeTag_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

