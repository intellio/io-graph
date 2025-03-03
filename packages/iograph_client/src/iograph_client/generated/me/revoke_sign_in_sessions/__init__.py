# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.revoke_sign_in_sessions_response import RevokeSignInSessionsResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class RevokeSignInSessionsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/revokeSignInSessions", path_parameters)

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> RevokeSignInSessionsResponse:
		"""
		Invoke action revokeSignInSessions
		Invalidates all the refresh tokens issued to applications for a user (as well as session cookies in a user's browser), by resetting the signInSessionsValidFromDateTime user property to the current date-time. Typically, this operation is performed (by the user or an administrator) if the user has a lost or stolen device. This operation prevents access to the organization's data through applications on the device by requiring the user to sign in again to all applications that they have previously consented to, independent of device.
		Find more info here: https://learn.microsoft.com/graph/api/user-revokesigninsessions?view=graph-rest-1.0
		"""
		tags = ['me.user.Actions']

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
		return await self.request_adapter.send_async(request_info, RevokeSignInSessionsResponse, error_mapping)


	def with_url(self, raw_url: str) -> RevokeSignInSessionsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RevokeSignInSessionsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RevokeSignInSessionsRequest(self.request_adapter, self.path_parameters)

