# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.models.get_mail_tips_post_request import Get_mail_tipsPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.get_mail_tips_response import GetMailTipsResponse


class GetMailTipsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/getMailTips"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Get_mail_tipsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> GetMailTipsResponse:
		"""
		Invoke action getMailTips
		Get the MailTips of one or more recipients as available to the signed-in user. Note that by making a POST call to the getMailTips action, you can request specific types of MailTips to
be returned for more than one recipient at one time. The requested MailTips are returned in a mailTips collection.
		Find more info here: https://learn.microsoft.com/graph/api/user-getmailtips?view=graph-rest-1.0
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


