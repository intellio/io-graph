# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.get_member_groups_post_response import Get_member_groupsPostResponse
from iograph_models.models.get_member_groups_post_request import Get_member_groupsPostRequest


class GetMemberGroupsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/devices/{device%2Did}/getMemberGroups", path_parameters)

	async def post(
		self,
		body: Get_member_groupsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> Get_member_groupsPostResponse:
		"""
		Invoke action getMemberGroups
		Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.
		Find more info here: https://learn.microsoft.com/graph/api/directoryobject-getmembergroups?view=graph-rest-1.0
		"""
		tags = ['devices.device.Actions']

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
		return await self.request_adapter.send_async(request_info, Get_member_groupsPostResponse, error_mapping)


	def with_url(self, raw_url: str) -> GetMemberGroupsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GetMemberGroupsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GetMemberGroupsRequest(self.request_adapter, self.path_parameters)

