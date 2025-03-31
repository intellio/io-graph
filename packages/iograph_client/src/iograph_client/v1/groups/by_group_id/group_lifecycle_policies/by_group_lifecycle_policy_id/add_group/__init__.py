# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.v1.add_group_post_response import Add_groupPostResponse
from iograph_models.v1.add_group_post_request import Add_groupPostRequest
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class AddGroupRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/groupLifecyclePolicies/{groupLifecyclePolicy%2Did}/addGroup", path_parameters)

	async def post(
		self,
		body: Add_groupPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Add_groupPostResponse:
		"""
		Invoke action addGroup
		Add a group to a groupLifecyclePolicy. This action is supported only if the managedGroupTypes property of the policy is set to Selected.
		Find more info here: https://learn.microsoft.com/graph/api/grouplifecyclepolicy-addgroup?view=graph-rest-1.0
		"""
		tags = ['groups.groupLifecyclePolicy']

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
		return await self.request_adapter.send_async(request_info, Add_groupPostResponse, error_mapping)


	def with_url(self, raw_url: str) -> AddGroupRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: AddGroupRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return AddGroupRequest(self.request_adapter, self.path_parameters)

