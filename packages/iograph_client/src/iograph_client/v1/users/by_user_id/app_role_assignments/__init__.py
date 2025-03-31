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
	from .by_app_role_assignment_id import ByAppRoleAssignmentIdRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.app_role_assignment_collection_response import AppRoleAssignmentCollectionResponse
from iograph_models.v1.app_role_assignment import AppRoleAssignment


class AppRoleAssignmentsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/appRoleAssignments", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AppRoleAssignmentCollectionResponse:
		"""
		List appRoleAssignments granted to a user
		Retrieve the list of appRoleAssignments that are currently granted to a user. This operation also returns app role assignments granted to groups that the user is a direct member of.
		Find more info here: https://learn.microsoft.com/graph/api/user-list-approleassignments?view=graph-rest-1.0
		"""
		tags = ['users.appRoleAssignment']
		header_parameters = [{'name': 'ConsistencyLevel', 'in': 'header', 'description': 'Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries', 'schema': {'type': 'string'}, 'examples': {'example-1': {'description': "$search and $count queries require the client to set the ConsistencyLevel HTTP header to 'eventual'.", 'value': 'eventual'}}}]

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
		return await self.request_adapter.send_async(request_info, AppRoleAssignmentCollectionResponse, error_mapping)

	async def post(
		self,
		body: AppRoleAssignment,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> AppRoleAssignment:
		"""
		Grant an appRoleAssignment to a user
		Assign an app role to a user, creating an appRoleAssignment object. To grant an app role assignment to a user, you need three identifiers:
		Find more info here: https://learn.microsoft.com/graph/api/user-post-approleassignments?view=graph-rest-1.0
		"""
		tags = ['users.appRoleAssignment']

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
		return await self.request_adapter.send_async(request_info, AppRoleAssignment, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> AppRoleAssignmentsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AppRoleAssignmentsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AppRoleAssignmentsRequest(self.request_adapter, self.path_parameters)

	def by_app_role_assignment_id(self,
		user_id: str,
		appRoleAssignment_id: str,
	) -> ByAppRoleAssignmentIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if appRoleAssignment_id is None:
			raise TypeError("appRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["appRoleAssignment%2Did"] =  appRoleAssignment_id

		from .by_app_role_assignment_id import ByAppRoleAssignmentIdRequest
		return ByAppRoleAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

