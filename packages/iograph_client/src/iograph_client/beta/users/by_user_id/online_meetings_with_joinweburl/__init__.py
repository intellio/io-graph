# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .send_virtual_appointment_sms import SendVirtualAppointmentSmsRequest
	from .send_virtual_appointment_reminder_sms import SendVirtualAppointmentReminderSmsRequest
	from .get_virtual_appointment_join_web_url import GetVirtualAppointmentJoinWebUrlRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.online_meeting import OnlineMeeting


class OnlineMeetingsWithJoinWebUrlRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onlineMeetings(joinWebUrl='{joinWebUrl}')", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> OnlineMeeting:
		"""
		Get onlineMeetings from users
		Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.
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
		return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)

	async def patch(
		self,
		body: OnlineMeeting,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> OnlineMeeting:
		"""
		Update the navigation property onlineMeetings in users
		
		"""
		tags = ['users.onlineMeeting']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.PATCH,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property onlineMeetings for users
		
		"""
		tags = ['users.onlineMeeting']
		header_parameters = [{'name': 'If-Match', 'in': 'header', 'description': 'ETag', 'schema': {'type': 'string'}}]

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.DELETE,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")



	def with_url(self, raw_url: str) -> OnlineMeetingsWithJoinWebUrlRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: OnlineMeetingsWithJoinWebUrlRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return OnlineMeetingsWithJoinWebUrlRequest(self.request_adapter, self.path_parameters)

	def get_virtual_appointment_join_web_url(self,
		user_id: str,
		joinWebUrl: str,
	) -> GetVirtualAppointmentJoinWebUrlRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .get_virtual_appointment_join_web_url import GetVirtualAppointmentJoinWebUrlRequest
		return GetVirtualAppointmentJoinWebUrlRequest(self.request_adapter, path_parameters)

	def send_virtual_appointment_reminder_sms(self,
		user_id: str,
		joinWebUrl: str,
	) -> SendVirtualAppointmentReminderSmsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .send_virtual_appointment_reminder_sms import SendVirtualAppointmentReminderSmsRequest
		return SendVirtualAppointmentReminderSmsRequest(self.request_adapter, path_parameters)

	def send_virtual_appointment_sms(self,
		user_id: str,
		joinWebUrl: str,
	) -> SendVirtualAppointmentSmsRequest:
		if user_id is None:
			raise TypeError("user_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["user%2Did"] =  user_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .send_virtual_appointment_sms import SendVirtualAppointmentSmsRequest
		return SendVirtualAppointmentSmsRequest(self.request_adapter, path_parameters)

