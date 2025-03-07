# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .cancel import CancelRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.models.virtual_event_registration import VirtualEventRegistration
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class RegistrationsWithUserIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/webinars/{virtualEventWebinar%2Did}/registrations(userId='{userId}')", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventRegistration:
		"""
		Get virtualEventRegistration
		Get the properties and relationships of a virtualEventRegistration object.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventregistration-get?view=graph-rest-1.0
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
		return await self.request_adapter.send_async(request_info, VirtualEventRegistration, error_mapping)

	async def patch(
		self,
		body: VirtualEventRegistration,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEventRegistration:
		"""
		Update the navigation property registrations in solutions
		
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
		return await self.request_adapter.send_async(request_info, VirtualEventRegistration, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property registrations for solutions
		
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



	def with_url(self, raw_url: str) -> RegistrationsWithUserIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RegistrationsWithUserIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RegistrationsWithUserIdRequest(self.request_adapter, self.path_parameters)

	def cancel(self,
		virtualEventWebinar_id: str,
		userId: str,
	) -> CancelRequest:
		if virtualEventWebinar_id is None:
			raise TypeError("virtualEventWebinar_id cannot be null.")
		if userId is None:
			raise TypeError("userId cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventWebinar%2Did"] =  virtualEventWebinar_id
		path_parameters["userId"] =  userId

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

