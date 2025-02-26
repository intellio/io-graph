# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.models.send_activity_notification_to_recipients_post_request import Send_activity_notification_to_recipientsPostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class SendActivityNotificationToRecipientsRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/teamwork/sendActivityNotificationToRecipients"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Send_activity_notification_to_recipientsPostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action sendActivityNotificationToRecipients
		Send activity feed notifications to multiple users, in bulk.  For more information, see sending Teams activity notifications.
		Find more info here: https://learn.microsoft.com/graph/api/teamwork-sendactivitynotificationtorecipients?view=graph-rest-1.0
		"""
		tags = ['teamwork.teamwork.Actions']

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


