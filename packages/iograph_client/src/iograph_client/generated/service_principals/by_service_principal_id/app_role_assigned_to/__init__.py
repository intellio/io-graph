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
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.app_role_assignment import AppRoleAssignment
from iograph_models.models.app_role_assignment_collection_response import AppRoleAssignmentCollectionResponse


class AppRoleAssignedToRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/appRoleAssignedTo", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> AppRoleAssignmentCollectionResponse:
		"""
		Get appRoleAssignment
		Read the properties and relationships of an appRoleAssignment object.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-list-approleassignedto?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.appRoleAssignment']

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
		Grant an appRoleAssignment for a service principal
		Assign an app role for a resource service principal, to a user, group, or client service principal. App roles that are assigned to service principals are also known as application permissions. Application permissions can be granted directly with app role assignments, or through a consent experience. To grant an app role assignment, you need three identifiers:
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-post-approleassignedto?view=graph-rest-1.0
		"""
		tags = ['servicePrincipals.appRoleAssignment']

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


	def with_url(self, raw_url: str) -> AppRoleAssignedToRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AppRoleAssignedToRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AppRoleAssignedToRequest(self.request_adapter, self.path_parameters)

	def by_app_role_assignment_id(self,
		servicePrincipal_id: str,
		appRoleAssignment_id: str,
	) -> ByAppRoleAssignmentIdRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")
		if appRoleAssignment_id is None:
			raise TypeError("appRoleAssignment_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id
		path_parameters["appRoleAssignment%2Did"] =  appRoleAssignment_id

		from .by_app_role_assignment_id import ByAppRoleAssignmentIdRequest
		return ByAppRoleAssignmentIdRequest(self.request_adapter, path_parameters)

	def count(self,
		servicePrincipal_id: str,
	) -> CountRequest:
		if servicePrincipal_id is None:
			raise TypeError("servicePrincipal_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["servicePrincipal%2Did"] =  servicePrincipal_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

