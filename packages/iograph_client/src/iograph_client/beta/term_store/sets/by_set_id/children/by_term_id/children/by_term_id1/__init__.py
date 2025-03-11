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
	from .set import SetRequest
	from .relations import RelationsRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.term_store_term import TermStoreTerm


class ByTermId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/termStore/sets/{set%2Did}/children/{term%2Did}/children/{term%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermStoreTerm:
		"""
		Get children from termStore
		Children of current term.
		"""
		tags = ['termStore.set']

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
		return await self.request_adapter.send_async(request_info, TermStoreTerm, error_mapping)

	async def patch(
		self,
		body: TermStoreTerm,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermStoreTerm:
		"""
		Update the navigation property children in termStore
		
		"""
		tags = ['termStore.set']

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
		return await self.request_adapter.send_async(request_info, TermStoreTerm, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property children for termStore
		
		"""
		tags = ['termStore.set']
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



	def with_url(self, raw_url: str) -> ByTermId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByTermId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByTermId1Request(self.request_adapter, self.path_parameters)

	def relations(self,
		set_id: str,
		term_id: str,
		term_id1: str,
	) -> RelationsRequest:
		if set_id is None:
			raise TypeError("set_id cannot be null.")
		if term_id is None:
			raise TypeError("term_id cannot be null.")
		if term_id1 is None:
			raise TypeError("term_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["set%2Did"] =  set_id
		path_parameters["term%2Did"] =  term_id
		path_parameters["term%2Did1"] =  term_id1

		from .relations import RelationsRequest
		return RelationsRequest(self.request_adapter, path_parameters)

	def set(self,
		set_id: str,
		term_id: str,
		term_id1: str,
	) -> SetRequest:
		if set_id is None:
			raise TypeError("set_id cannot be null.")
		if term_id is None:
			raise TypeError("term_id cannot be null.")
		if term_id1 is None:
			raise TypeError("term_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["set%2Did"] =  set_id
		path_parameters["term%2Did"] =  term_id
		path_parameters["term%2Did1"] =  term_id1

		from .set import SetRequest
		return SetRequest(self.request_adapter, path_parameters)

