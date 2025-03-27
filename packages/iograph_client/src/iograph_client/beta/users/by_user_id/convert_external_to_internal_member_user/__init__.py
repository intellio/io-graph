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
from iograph_models.beta.convert_external_to_internal_member_user_post_request import Convert_external_to_internal_member_userPostRequest
from iograph_models.beta.convert_external_to_internal_member_user_response import ConvertExternalToInternalMemberUserResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ConvertExternalToInternalMemberUserRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/convertExternalToInternalMemberUser", path_parameters)

	async def post(
		self,
		body: Convert_external_to_internal_member_userPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> ConvertExternalToInternalMemberUserResponse:
		"""
		Invoke action convertExternalToInternalMemberUser
		Convert an externally authenticated user into an internal user. The user is able to sign into the host tenant as an internal user and access resources as a member. For more information about this conversion, see Convert external users to internal users.
		Find more info here: https://learn.microsoft.com/graph/api/user-convertexternaltointernalmemberuser?view=graph-rest-beta
		"""
		tags = ['users.user.Actions']

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
		return await self.request_adapter.send_async(request_info, ConvertExternalToInternalMemberUserResponse, error_mapping)


	def with_url(self, raw_url: str) -> ConvertExternalToInternalMemberUserRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ConvertExternalToInternalMemberUserRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ConvertExternalToInternalMemberUserRequest(self.request_adapter, self.path_parameters)

