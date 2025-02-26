# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.set_user_preferred_presence_post_request import Set_user_preferred_presencePostRequest
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class SetUserPreferredPresenceRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/users/{user%2Did}/presence/setUserPreferredPresence"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: Set_user_preferred_presencePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Invoke action setUserPreferredPresence
		Set the preferred availability and activity status for a user. If the preferred presence of a user is set, the user's presence shows as the preferred status. Preferred presence takes effect only when at least one presence session exists for the user. Otherwise, the user's presence shows as Offline. A presence session is created as a result of a successful setPresence operation, or if the user is signed in on a Microsoft Teams client. For more details, see presence sessions and time-out and expiration.
		Find more info here: https://learn.microsoft.com/graph/api/presence-setuserpreferredpresence?view=graph-rest-1.0
		"""
		tags = ['users.presence']

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


