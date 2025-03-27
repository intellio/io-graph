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
	from .remove_group import RemoveGroupRequest
	from .add_group import AddGroupRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.group_lifecycle_policy import GroupLifecyclePolicy


class ByGroupLifecyclePolicyIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/groupLifecyclePolicies/{groupLifecyclePolicy%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> GroupLifecyclePolicy:
		"""
		Get groupLifecyclePolicies from groups
		The collection of lifecycle policies for this group. Read-only. Nullable.
		"""
		tags = ['groups.groupLifecyclePolicy']

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
		return await self.request_adapter.send_async(request_info, GroupLifecyclePolicy, error_mapping)

	async def patch(
		self,
		body: GroupLifecyclePolicy,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GroupLifecyclePolicy:
		"""
		Update the navigation property groupLifecyclePolicies in groups
		
		"""
		tags = ['groups.groupLifecyclePolicy']

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
		return await self.request_adapter.send_async(request_info, GroupLifecyclePolicy, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property groupLifecyclePolicies for groups
		
		"""
		tags = ['groups.groupLifecyclePolicy']
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



	def with_url(self, raw_url: str) -> ByGroupLifecyclePolicyIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupLifecyclePolicyIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupLifecyclePolicyIdRequest(self.request_adapter, self.path_parameters)

	def add_group(self,
		group_id: str,
		groupLifecyclePolicy_id: str,
	) -> AddGroupRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if groupLifecyclePolicy_id is None:
			raise TypeError("groupLifecyclePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["groupLifecyclePolicy%2Did"] =  groupLifecyclePolicy_id

		from .add_group import AddGroupRequest
		return AddGroupRequest(self.request_adapter, path_parameters)

	def remove_group(self,
		group_id: str,
		groupLifecyclePolicy_id: str,
	) -> RemoveGroupRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if groupLifecyclePolicy_id is None:
			raise TypeError("groupLifecyclePolicy_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["groupLifecyclePolicy%2Did"] =  groupLifecyclePolicy_id

		from .remove_group import RemoveGroupRequest
		return RemoveGroupRequest(self.request_adapter, path_parameters)

