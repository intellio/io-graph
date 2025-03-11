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
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.user_registration_method_summary import UserRegistrationMethodSummary


class UsersRegisteredByMethodRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/reports/authenticationMethods/usersRegisteredByMethod()", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UserRegistrationMethodSummary:
		"""
		Invoke function usersRegisteredByMethod
		Get the number of users registered for each authentication method.
		Find more info here: https://learn.microsoft.com/graph/api/authenticationmethodsroot-usersregisteredbymethod?view=graph-rest-1.0
		"""
		tags = ['reports.authenticationMethodsRoot']

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
		return await self.request_adapter.send_async(request_info, UserRegistrationMethodSummary, error_mapping)


	def with_url(self, raw_url: str) -> UsersRegisteredByMethodRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UsersRegisteredByMethodRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UsersRegisteredByMethodRequest(self.request_adapter, self.path_parameters)

