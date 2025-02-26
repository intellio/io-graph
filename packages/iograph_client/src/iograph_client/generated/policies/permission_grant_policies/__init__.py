# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_permission_grant_policy_id import ByPermissionGrantPolicyIdRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.permission_grant_policy import PermissionGrantPolicy
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.permission_grant_policy_collection_response import PermissionGrantPolicyCollectionResponse


class PermissionGrantPoliciesRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/policies/permissionGrantPolicies"
		self.path_parameters: dict[str, Any] = path_parameters

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PermissionGrantPolicyCollectionResponse:
		"""
		List permissionGrantPolicies
		Retrieve the list of permissionGrantPolicy objects.
		Find more info here: https://learn.microsoft.com/graph/api/permissiongrantpolicy-list?view=graph-rest-1.0
		"""
		tags = ['policies.permissionGrantPolicy']

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
		return await self.request_adapter.send_async(request_info, PermissionGrantPolicyCollectionResponse, error_mapping)

	async def post(
		self,
		body: PermissionGrantPolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PermissionGrantPolicy:
		"""
		Create permissionGrantPolicy
		Creates a permissionGrantPolicy. A permission grant policy is used to describe the conditions under which permissions can be granted (for example, during application consent). After creating the permission grant policy, you can add include condition sets to add matching rules, and add exclude condition sets to add exclusion rules.
		Find more info here: https://learn.microsoft.com/graph/api/permissiongrantpolicy-post-permissiongrantpolicies?view=graph-rest-1.0
		"""
		tags = ['policies.permissionGrantPolicy']

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
		return await self.request_adapter.send_async(request_info, PermissionGrantPolicy, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def by_permission_grant_policy_id(self,
		permissionGrantPolicy_id: str,
	) -> ByPermissionGrantPolicyIdRequest:
		if permissionGrantPolicy_id is None:
			raise TypeError("permissionGrantPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["permissionGrantPolicy%2Did"] =  permissionGrantPolicy_id

		from .by_permission_grant_policy_id import ByPermissionGrantPolicyIdRequest
		return ByPermissionGrantPolicyIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

