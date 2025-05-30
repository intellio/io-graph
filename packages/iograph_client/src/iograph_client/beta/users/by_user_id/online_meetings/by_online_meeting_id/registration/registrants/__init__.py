# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_meeting_registrant_base_id import ByMeetingRegistrantBaseIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.meeting_registrant_base import MeetingRegistrantBase
from iograph_models.beta.meeting_registrant_base_collection_response import MeetingRegistrantBaseCollectionResponse


class RegistrantsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onlineMeetings/{onlineMeeting%2Did}/registration/registrants", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MeetingRegistrantBaseCollectionResponse:
		"""
		Get registrants from users
		Registrants of the online meeting.
		"""
		tags = ['users.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, MeetingRegistrantBaseCollectionResponse, error_mapping)

	async def post(
		self,
		body: MeetingRegistrantBase,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MeetingRegistrantBase:
		"""
		Create meetingRegistrant (deprecated)
		Enroll a meeting registrant in an online meeting that has meeting registration enabled on behalf of the registrant. This operation has two scenarios: In either scenario, the registrant will receive an email notification that contains their registration information.
		Find more info here: https://learn.microsoft.com/graph/api/meetingregistration-post-registrants?view=graph-rest-beta
		"""
		tags = ['users.onlineMeeting']

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
		return await self.request_adapter.send_async(request_info, MeetingRegistrantBase, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RegistrantsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RegistrantsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RegistrantsRequest(self.request_adapter, self.path_parameters)

	def by_meeting_registrant_base_id(self,
		user_id: str,
		onlineMeeting_id: str,
		meetingRegistrantBase_id: str,
	) -> ByMeetingRegistrantBaseIdRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")
		if meetingRegistrantBase_id is None:
			raise TypeError("meetingRegistrantBase_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id
		path_parameters["meetingRegistrantBase%2Did"] =  meetingRegistrantBase_id

		from .by_meeting_registrant_base_id import ByMeetingRegistrantBaseIdRequest
		return ByMeetingRegistrantBaseIdRequest(self.request_adapter, path_parameters)

	def count(self,
		user_id: str,
		onlineMeeting_id: str,
	) -> CountRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if onlineMeeting_id is None:
			raise TypeError("onlineMeeting_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["onlineMeeting%2Did"] =  onlineMeeting_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

