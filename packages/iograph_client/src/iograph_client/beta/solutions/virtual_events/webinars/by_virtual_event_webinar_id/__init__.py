# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sessions_with_joinweburl import SessionsWithJoinWebUrlRequest
	from .sessions import SessionsRequest
	from .registrations_with_userid import RegistrationsWithUserIdRequest
	from .registrations_with_email import RegistrationsWithEmailRequest
	from .registrations import RegistrationsRequest
	from .registration_configuration import RegistrationConfigurationRequest
	from .presenters import PresentersRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.virtual_event_webinar import VirtualEventWebinar
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByVirtualEventWebinarIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventWebinar:
		"""
		Get virtualEventWebinar
		Read the properties and relationships of a virtualEventWebinar object.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventwebinar-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, VirtualEventWebinar, error_mapping)

	async def patch(
		self,
		body: VirtualEventWebinar,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEventWebinar:
		"""
		Update virtualEventWebinar
		Update the properties of a virtualEventWebinar object.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventwebinar-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, VirtualEventWebinar, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property webinars for solutions
		
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



	def with_url(self, raw_url: str) -> ByVirtualEventWebinarIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByVirtualEventWebinarIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByVirtualEventWebinarIdRequest(self.request_adapter, self.path_parameters)

	def presenters(self,
		virtualEventWebinar_id: str,
	) -> PresentersRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id

		from .presenters import PresentersRequest
		return PresentersRequest(self.request_adapter, path_parameters)

	def registration_configuration(self,
		virtualEventWebinar_id: str,
	) -> RegistrationConfigurationRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id

		from .registration_configuration import RegistrationConfigurationRequest
		return RegistrationConfigurationRequest(self.request_adapter, path_parameters)

	def registrations(self,
		virtualEventWebinar_id: str,
	) -> RegistrationsRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id

		from .registrations import RegistrationsRequest
		return RegistrationsRequest(self.request_adapter, path_parameters)

	def registrations_with_email(self,
		virtualEventWebinar_id: str,
		email: str,
	) -> RegistrationsWithEmailRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")
		if email is None:
			raise TypeError("email cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id
		path_parameters["email"] =  email

		from .registrations_with_email import RegistrationsWithEmailRequest
		return RegistrationsWithEmailRequest(self.request_adapter, path_parameters)

	def registrations_with_userid(self,
		virtualEventWebinar_id: str,
		userId: str,
	) -> RegistrationsWithUserIdRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")
		if userId is None:
			raise TypeError("userId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id
		path_parameters["userId"] =  userId

		from .registrations_with_userid import RegistrationsWithUserIdRequest
		return RegistrationsWithUserIdRequest(self.request_adapter, path_parameters)

	def sessions(self,
		virtualEventWebinar_id: str,
	) -> SessionsRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id

		from .sessions import SessionsRequest
		return SessionsRequest(self.request_adapter, path_parameters)

	def sessions_with_joinweburl(self,
		virtualEventWebinar_id: str,
		joinWebUrl: str,
	) -> SessionsWithJoinWebUrlRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .sessions_with_joinweburl import SessionsWithJoinWebUrlRequest
		return SessionsWithJoinWebUrlRequest(self.request_adapter, path_parameters)

