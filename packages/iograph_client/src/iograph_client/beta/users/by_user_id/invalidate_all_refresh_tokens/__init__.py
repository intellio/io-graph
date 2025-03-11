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
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.invalidate_all_refresh_tokens_response import InvalidateAllRefreshTokensResponse


class InvalidateAllRefreshTokensRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/invalidateAllRefreshTokens", path_parameters)

	async def post(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> InvalidateAllRefreshTokensResponse:
		"""
		Invoke action invalidateAllRefreshTokens
		Invalidates all of the user's refresh tokens issued to applications and session cookies in a user's browser, by resetting the refreshTokensValidFromDateTime user property to the current date-time. Typically, this operation is performed (by the user or an administrator) if the user has a lost or stolen device. This operation would prevent access to any of the organization's data accessed through applications on the device without the user first being required to sign in again. In fact, this operation would force the user to sign in again for all applications that they have previously consented to, independent of device. For developers, if the application attempts to redeem a delegated access token for this user by using an invalidated refresh token, the application receives an error. If this happens, the application needs to acquire a new refresh token by making a request to the OAuth 2.0 /authorize endpoint, which forces the user to sign in.
		Find more info here: https://learn.microsoft.com/graph/api/user-invalidateallrefreshtokens?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, InvalidateAllRefreshTokensResponse, error_mapping)


	def with_url(self, raw_url: str) -> InvalidateAllRefreshTokensRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: InvalidateAllRefreshTokensRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return InvalidateAllRefreshTokensRequest(self.request_adapter, self.path_parameters)

