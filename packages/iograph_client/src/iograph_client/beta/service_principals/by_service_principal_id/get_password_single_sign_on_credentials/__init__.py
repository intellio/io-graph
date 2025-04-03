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
from iograph_models.beta.get_password_single_sign_on_credentials_post_request import Get_password_single_sign_on_credentialsPostRequest
from iograph_models.beta.password_single_sign_on_credential_set import PasswordSingleSignOnCredentialSet


class GetPasswordSingleSignOnCredentialsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/getPasswordSingleSignOnCredentials", path_parameters)

	async def post(
		self,
		body: Get_password_single_sign_on_credentialsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> PasswordSingleSignOnCredentialSet:
		"""
		Invoke action getPasswordSingleSignOnCredentials
		Get a list of single sign-on credentials using a password for a user or group.
		Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-getpasswordsinglesignoncredentials?view=graph-rest-beta
		"""
		tags = ['servicePrincipals.servicePrincipal.Actions']

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
		return await self.request_adapter.send_async(request_info, PasswordSingleSignOnCredentialSet, error_mapping)


	def with_url(self, raw_url: str) -> GetPasswordSingleSignOnCredentialsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GetPasswordSingleSignOnCredentialsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GetPasswordSingleSignOnCredentialsRequest(self.request_adapter, self.path_parameters)

