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
	from .delta import DeltaRequest
	from .count import CountRequest
	from .by_event_id1 import ByEventId1Request
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.event_collection_response import EventCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ExceptionOccurrencesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/me/events/{event%2Did}/exceptionOccurrences", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EventCollectionResponse:
		"""
		Get exceptionOccurrences from me
		
		"""
		tags = ['me.event']

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
		return await self.request_adapter.send_async(request_info, EventCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> ExceptionOccurrencesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ExceptionOccurrencesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ExceptionOccurrencesRequest(self.request_adapter, self.path_parameters)

	def by_event_id1(self,
		event_id: str,
		event_id1: str,
	) -> ByEventId1Request:
		if event_id is None:
			raise TypeError("event_id cannot be null.")
		if event_id1 is None:
			raise TypeError("event_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id
		path_parameters["event%2Did1"] =  event_id1

		from .by_event_id1 import ByEventId1Request
		return ByEventId1Request(self.request_adapter, path_parameters)

	def count(self,
		event_id: str,
	) -> CountRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

	def delta(self,
		event_id: str,
	) -> DeltaRequest:
		if event_id is None:
			raise TypeError("event_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["event%2Did"] =  event_id

		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, path_parameters)

