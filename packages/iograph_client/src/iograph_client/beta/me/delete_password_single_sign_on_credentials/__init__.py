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
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.delete_password_single_sign_on_credentials_post_request import Delete_password_single_sign_on_credentialsPostRequest


class DeletePasswordSingleSignOnCredentialsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/deletePasswordSingleSignOnCredentials", path_parameters)

	async def post(
		self,
		body: Delete_password_single_sign_on_credentialsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action deletePasswordSingleSignOnCredentials
		Delete the password-based single sign-on credentials for a given user to a given service principal.
		Find more info here: https://learn.microsoft.com/graph/api/user-deletepasswordsinglesignoncredentials?view=graph-rest-beta
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
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> DeletePasswordSingleSignOnCredentialsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeletePasswordSingleSignOnCredentialsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeletePasswordSingleSignOnCredentialsRequest(self.request_adapter, self.path_parameters)

