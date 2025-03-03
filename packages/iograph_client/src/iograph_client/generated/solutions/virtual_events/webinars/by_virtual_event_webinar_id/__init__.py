# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sessions import SessionsRequest
	from .registrations import RegistrationsRequest
	from .registration_configuration import RegistrationConfigurationRequest
	from .presenters import PresentersRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.models.virtual_event_webinar import VirtualEventWebinar
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class ByVirtualEventWebinarIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventWebinar:
		"""
		Get virtualEventWebinar
		Read the properties and relationships of a virtualEventWebinar object. All roles can get the details of a webinar event.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventwebinar-get?view=graph-rest-1.0
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
		Update the properties of a virtualEventWebinar object. Only the Organizer and Co-organizer can make changes to a webinar event.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventwebinar-update?view=graph-rest-1.0
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

	@property
	def presenters(self,
	) -> PresentersRequest:
		from .presenters import PresentersRequest
		return PresentersRequest(self.request_adapter, self.path_parameters)

	@property
	def registration_configuration(self,
	) -> RegistrationConfigurationRequest:
		from .registration_configuration import RegistrationConfigurationRequest
		return RegistrationConfigurationRequest(self.request_adapter, self.path_parameters)

	@property
	def registrations(self,
	) -> RegistrationsRequest:
		from .registrations import RegistrationsRequest
		return RegistrationsRequest(self.request_adapter, self.path_parameters)

	@property
	def sessions(self,
	) -> SessionsRequest:
		from .sessions import SessionsRequest
		return SessionsRequest(self.request_adapter, self.path_parameters)

