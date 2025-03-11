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
	from .presenters import PresentersRequest
	from .set_external_event_information import SetExternalEventInformationRequest
	from .publish import PublishRequest
	from .cancel import CancelRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.virtual_event import VirtualEvent


class ByVirtualEventIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/events/{virtualEvent%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEvent:
		"""
		Get events from solutions
		
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
		return await self.request_adapter.send_async(request_info, VirtualEvent, error_mapping)

	async def patch(
		self,
		body: VirtualEvent,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEvent:
		"""
		Update the navigation property events in solutions
		
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
		return await self.request_adapter.send_async(request_info, VirtualEvent, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property events for solutions
		
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



	def with_url(self, raw_url: str) -> ByVirtualEventIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByVirtualEventIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByVirtualEventIdRequest(self.request_adapter, self.path_parameters)

	def cancel(self,
		virtualEvent_id: str,
	) -> CancelRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id

		from .cancel import CancelRequest
		return CancelRequest(self.request_adapter, path_parameters)

	def publish(self,
		virtualEvent_id: str,
	) -> PublishRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id

		from .publish import PublishRequest
		return PublishRequest(self.request_adapter, path_parameters)

	def set_external_event_information(self,
		virtualEvent_id: str,
	) -> SetExternalEventInformationRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id

		from .set_external_event_information import SetExternalEventInformationRequest
		return SetExternalEventInformationRequest(self.request_adapter, path_parameters)

	def presenters(self,
		virtualEvent_id: str,
	) -> PresentersRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id

		from .presenters import PresentersRequest
		return PresentersRequest(self.request_adapter, path_parameters)

	def sessions(self,
		virtualEvent_id: str,
	) -> SessionsRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id

		from .sessions import SessionsRequest
		return SessionsRequest(self.request_adapter, path_parameters)

	def sessions_with_joinweburl(self,
		virtualEvent_id: str,
		joinWebUrl: str,
	) -> SessionsWithJoinWebUrlRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .sessions_with_joinweburl import SessionsWithJoinWebUrlRequest
		return SessionsWithJoinWebUrlRequest(self.request_adapter, path_parameters)

