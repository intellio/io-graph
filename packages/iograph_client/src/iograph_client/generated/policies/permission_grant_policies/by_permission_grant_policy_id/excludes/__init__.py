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
	from .by_permission_grant_condition_set_id import ByPermissionGrantConditionSetIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.permission_grant_condition_set_collection_response import PermissionGrantConditionSetCollectionResponse
from iograph_models.models.permission_grant_condition_set import PermissionGrantConditionSet


class ExcludesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/policies/permissionGrantPolicies/{permissionGrantPolicy%2Did}/excludes", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> PermissionGrantConditionSetCollectionResponse:
		"""
		List excludes collection of permissionGrantPolicy
		Retrieve the condition sets which are *excluded* in a permissionGrantPolicy.
		Find more info here: https://learn.microsoft.com/graph/api/permissiongrantpolicy-list-excludes?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, PermissionGrantConditionSetCollectionResponse, error_mapping)

	async def post(
		self,
		body: PermissionGrantConditionSet,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PermissionGrantConditionSet:
		"""
		Create permissionGrantConditionSet in excludes collection of permissionGrantPolicy
		Add conditions under which a permission grant event is *excluded* in a permission grant policy. You do this by adding a permissionGrantConditionSet to the excludes collection of a  permissionGrantPolicy.
		Find more info here: https://learn.microsoft.com/graph/api/permissiongrantpolicy-post-excludes?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, PermissionGrantConditionSet, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> ExcludesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ExcludesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ExcludesRequest(self.request_adapter, self.path_parameters)

	def by_permission_grant_condition_set_id(self,
		permissionGrantPolicy_id: str,
		permissionGrantConditionSet_id: str,
	) -> ByPermissionGrantConditionSetIdRequest:
		if permissionGrantPolicy_id is None:
			raise TypeError("permissionGrantPolicy_id cannot be null.")
		if permissionGrantConditionSet_id is None:
			raise TypeError("permissionGrantConditionSet_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["permissionGrantPolicy%2Did"] =  permissionGrantPolicy_id
		path_parameters["permissionGrantConditionSet%2Did"] =  permissionGrantConditionSet_id

		from .by_permission_grant_condition_set_id import ByPermissionGrantConditionSetIdRequest
		return ByPermissionGrantConditionSetIdRequest(self.request_adapter, path_parameters)

	def count(self,
		permissionGrantPolicy_id: str,
	) -> CountRequest:
		if permissionGrantPolicy_id is None:
			raise TypeError("permissionGrantPolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["permissionGrantPolicy%2Did"] =  permissionGrantPolicy_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

