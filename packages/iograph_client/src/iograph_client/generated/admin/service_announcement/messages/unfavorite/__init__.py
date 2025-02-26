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
from iograph_models.models.unfavorite_post_response import UnfavoritePostResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.unfavorite_post_request import UnfavoritePostRequest


class UnfavoriteRequest:
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		self.request_adapter = request_adapter
		self.url_template: str = "{+baseurl}/admin/serviceAnnouncement/messages/unfavorite"
		self.path_parameters: dict[str, Any] = path_parameters

	async def post(
		self,
		body: UnfavoritePostRequest,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> UnfavoritePostResponse:
		"""
		Invoke action unfavorite
		Remove the favorite status of serviceUpdateMessages for the signed in user.
		Find more info here: https://learn.microsoft.com/graph/api/serviceupdatemessage-unfavorite?view=graph-rest-1.0
		"""
		tags = ['admin.serviceAnnouncement']

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
		return await self.request_adapter.send_async(request_info, UnfavoritePostResponse, error_mapping)


