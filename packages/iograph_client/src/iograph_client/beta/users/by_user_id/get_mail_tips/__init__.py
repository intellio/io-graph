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
from iograph_models.beta.get_mail_tips_response import GetMailTipsResponse
from iograph_models.beta.get_mail_tips_post_request import Get_mail_tipsPostRequest


class GetMailTipsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/getMailTips", path_parameters)

	async def post(
		self,
		body: Get_mail_tipsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GetMailTipsResponse:
		"""
		Invoke action getMailTips
		Get the MailTips of one or more recipients as available to the signed-in user. Note that by making a POST call to the getMailTips action, you can request specific types of MailTips to
be returned for more than one recipient at one time. The requested MailTips are returned in a mailTips collection.
		Find more info here: https://learn.microsoft.com/graph/api/user-getmailtips?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, GetMailTipsResponse, error_mapping)


	def with_url(self, raw_url: str) -> GetMailTipsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: GetMailTipsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return GetMailTipsRequest(self.request_adapter, self.path_parameters)

