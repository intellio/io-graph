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
	from .registrations_with_userid import RegistrationsWithUserIdRequest
	from .registrations_with_email import RegistrationsWithEmailRequest
	from .registrations import RegistrationsRequest
	from .presenters import PresentersRequest
	from .attendance_reports import AttendanceReportsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.virtual_event_session import VirtualEventSession


class ByVirtualEventSessionIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/events/{virtualEvent%2Did}/sessions/{virtualEventSession%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventSession:
		"""
		Get sessions from solutions
		The sessions for the virtual event.
		"""
		tags = ['solutions.virtualEventsRoot']

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
		return await self.request_adapter.send_async(request_info, VirtualEventSession, error_mapping)

	async def patch(
		self,
		body: VirtualEventSession,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEventSession:
		"""
		Update the navigation property sessions in solutions
		
		"""
		tags = ['solutions.virtualEventsRoot']

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
		return await self.request_adapter.send_async(request_info, VirtualEventSession, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property sessions for solutions
		
		"""
		tags = ['solutions.virtualEventsRoot']
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



	def with_url(self, raw_url: str) -> ByVirtualEventSessionIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByVirtualEventSessionIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByVirtualEventSessionIdRequest(self.request_adapter, self.path_parameters)

	def attendance_reports(self,
		virtualEvent_id: str,
		virtualEventSession_id: str,
	) -> AttendanceReportsRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventSession_id is None:
			raise TypeError("virtualEventSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventSession%2Did"] =  virtualEventSession_id

		from .attendance_reports import AttendanceReportsRequest
		return AttendanceReportsRequest(self.request_adapter, path_parameters)

	def presenters(self,
		virtualEvent_id: str,
		virtualEventSession_id: str,
	) -> PresentersRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventSession_id is None:
			raise TypeError("virtualEventSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventSession%2Did"] =  virtualEventSession_id

		from .presenters import PresentersRequest
		return PresentersRequest(self.request_adapter, path_parameters)

	def registrations(self,
		virtualEvent_id: str,
		virtualEventSession_id: str,
	) -> RegistrationsRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventSession_id is None:
			raise TypeError("virtualEventSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventSession%2Did"] =  virtualEventSession_id

		from .registrations import RegistrationsRequest
		return RegistrationsRequest(self.request_adapter, path_parameters)

	def registrations_with_email(self,
		virtualEvent_id: str,
		virtualEventSession_id: str,
		email: str,
	) -> RegistrationsWithEmailRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventSession_id is None:
			raise TypeError("virtualEventSession_id cannot be null.")
		if email is None:
			raise TypeError("email cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventSession%2Did"] =  virtualEventSession_id
		path_parameters["email"] =  email

		from .registrations_with_email import RegistrationsWithEmailRequest
		return RegistrationsWithEmailRequest(self.request_adapter, path_parameters)

	def registrations_with_userid(self,
		virtualEvent_id: str,
		virtualEventSession_id: str,
		userId: str,
	) -> RegistrationsWithUserIdRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventSession_id is None:
			raise TypeError("virtualEventSession_id cannot be null.")
		if userId is None:
			raise TypeError("userId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventSession%2Did"] =  virtualEventSession_id
		path_parameters["userId"] =  userId

		from .registrations_with_userid import RegistrationsWithUserIdRequest
		return RegistrationsWithUserIdRequest(self.request_adapter, path_parameters)

