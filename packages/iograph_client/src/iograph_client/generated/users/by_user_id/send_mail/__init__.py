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
from iograph_models.models.send_mail_post_request import Send_mailPostRequest


class SendMailRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/sendMail", path_parameters)

	async def post(
		self,
		body: Send_mailPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action sendMail
		Send the message specified in the request body using either JSON or MIME format. When using JSON format, you can include a file attachment in the same sendMail action call. When using MIME format: This method saves the message in the Sent Items folder. Alternatively, create a draft message to send later. To learn more about the steps involved in the backend before a mail is delivered to recipients, see here.
		Find more info here: https://learn.microsoft.com/graph/api/user-sendmail?view=graph-rest-1.0
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
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)


	def with_url(self, raw_url: str) -> SendMailRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SendMailRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SendMailRequest(self.request_adapter, self.path_parameters)

