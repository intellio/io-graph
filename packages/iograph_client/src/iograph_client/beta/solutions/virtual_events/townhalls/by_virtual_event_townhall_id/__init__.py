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
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.virtual_event_townhall import VirtualEventTownhall


class ByVirtualEventTownhallIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/solutions/virtualEvents/townhalls/{virtualEventTownhall%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEventTownhall:
		"""
		Get virtualEventTownhall
		Read the properties and relationships of a virtualEventTownhall object.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventtownhall-get?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, VirtualEventTownhall, error_mapping)

	async def patch(
		self,
		body: VirtualEventTownhall,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEventTownhall:
		"""
		Update virtualEventTownhall
		Update the properties of a virtualEventTownhall object.
		Find more info here: https://learn.microsoft.com/graph/api/virtualeventtownhall-update?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, VirtualEventTownhall, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property townhalls for solutions
		
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



	def with_url(self, raw_url: str) -> ByVirtualEventTownhallIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByVirtualEventTownhallIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByVirtualEventTownhallIdRequest(self.request_adapter, self.path_parameters)

	def presenters(self,
		virtualEventTownhall_id: str,
	) -> PresentersRequest:
		if virtualEventTownhall_id is None:
			raise TypeError("virtualEventTownhall_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventTownhall%2Did"] =  virtualEventTownhall_id

		from .presenters import PresentersRequest
		return PresentersRequest(self.request_adapter, path_parameters)

	def sessions(self,
		virtualEventTownhall_id: str,
	) -> SessionsRequest:
		if virtualEventTownhall_id is None:
			raise TypeError("virtualEventTownhall_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventTownhall%2Did"] =  virtualEventTownhall_id

		from .sessions import SessionsRequest
		return SessionsRequest(self.request_adapter, path_parameters)

	def sessions_with_joinweburl(self,
		virtualEventTownhall_id: str,
		joinWebUrl: str,
	) -> SessionsWithJoinWebUrlRequest:
		if virtualEventTownhall_id is None:
			raise TypeError("virtualEventTownhall_id cannot be null.")
		if joinWebUrl is None:
			raise TypeError("joinWebUrl cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["virtualEventTownhall%2Did"] =  virtualEventTownhall_id
		path_parameters["joinWebUrl"] =  joinWebUrl

		from .sessions_with_joinweburl import SessionsWithJoinWebUrlRequest
		return SessionsWithJoinWebUrlRequest(self.request_adapter, path_parameters)

