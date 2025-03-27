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
	from .sessions_with_joinweburl import SessionsWithJoinWebUrlRequest
	from .sessions import SessionsRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.virtual_event_presenter import VirtualEventPresenter


class ByVirtualEventPresenterIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/events/{virtualEvent%2Did}/presenters/{virtualEventPresenter%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventPresenter:
		"""
		Get presenters from solutions
		The virtual event presenters.
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
		return await self.request_adapter.send_async(request_info, VirtualEventPresenter, error_mapping)

	async def patch(
		self,
		body: VirtualEventPresenter,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEventPresenter:
		"""
		Update the navigation property presenters in solutions
		
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
		return await self.request_adapter.send_async(request_info, VirtualEventPresenter, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property presenters for solutions
		
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



	def with_url(self, raw_url: str) -> ByVirtualEventPresenterIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByVirtualEventPresenterIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByVirtualEventPresenterIdRequest(self.request_adapter, self.path_parameters)

	def sessions(self,
		virtualEvent_id: str,
		virtualEventPresenter_id: str,
	) -> SessionsRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventPresenter_id is None:
			raise TypeError("virtualEventPresenter_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventPresenter%2Did"] =  virtualEventPresenter_id

		from .sessions import SessionsRequest
		return SessionsRequest(self.request_adapter, path_parameters)

	def sessions_with_joinweburl(self,
		virtualEvent_id: str,
		virtualEventPresenter_id: str,
		joinWebUrl: str,
	) -> SessionsWithJoinWebUrlRequest:
		if virtualEvent_id is None:
			raise TypeError("virtualEvent_id cannot be null.")
		if virtualEventPresenter_id is None:
			raise TypeError("virtualEventPresenter_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEvent%2Did"] =  virtualEvent_id
		path_parameters["virtualEventPresenter%2Did"] =  virtualEventPresenter_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .sessions_with_joinweburl import SessionsWithJoinWebUrlRequest
		return SessionsWithJoinWebUrlRequest(self.request_adapter, path_parameters)

