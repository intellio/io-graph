# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_virtual_event_registration_id import ByVirtualEventRegistrationIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.virtual_event_registration_collection_response import VirtualEventRegistrationCollectionResponse


class RegistrationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/events/{virtualEvent%2Did}/sessions/{virtualEventSession%2Did}/registrations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventRegistrationCollectionResponse:
		"""
		Get registrations from solutions
		
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
		return await self.request_adapter.send_async(request_info, VirtualEventRegistrationCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> RegistrationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RegistrationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RegistrationsRequest(self.request_adapter, self.path_parameters)

	def by_virtual_event_registration_id(self,
		virtualEvent_id: str,
		virtualEventSession_id: str,
		virtualEventRegistration_id: str,
	) -> ByVirtualEventRegistrationIdRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventSession_id is None:
			raise TypeError("virtualEventSession_id cannot be null.")
		if virtualEventRegistration_id is None:
			raise TypeError("virtualEventRegistration_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventSession%2Did"] =  virtualEventSession_id
		path_parameters["virtualEventRegistration%2Did"] =  virtualEventRegistration_id

		from .by_virtual_event_registration_id import ByVirtualEventRegistrationIdRequest
		return ByVirtualEventRegistrationIdRequest(self.request_adapter, path_parameters)

	def count(self,
		virtualEvent_id: str,
		virtualEventSession_id: str,
	) -> CountRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventSession_id is None:
			raise TypeError("virtualEventSession_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventSession%2Did"] =  virtualEventSession_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

