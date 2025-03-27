# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ................request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .to_term import ToTermRequest
	from .set import SetRequest
	from .from_term import FromTermRequest
	from ................request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.term_store_relation import TermStoreRelation


class ByRelationIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/termStores/{store%2Did}/groups/{group%2Did}/sets/{set%2Did}/terms/{term%2Did}/children/{term%2Did1}/relations/{relation%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermStoreRelation:
		"""
		Get relations from sites
		To indicate which terms are related to the current term as either pinned or reused.
		"""
		tags = ['sites.store']

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
		return await self.request_adapter.send_async(request_info, TermStoreRelation, error_mapping)

	async def patch(
		self,
		body: TermStoreRelation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermStoreRelation:
		"""
		Update the navigation property relations in sites
		
		"""
		tags = ['sites.store']

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
		return await self.request_adapter.send_async(request_info, TermStoreRelation, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property relations for sites
		
		"""
		tags = ['sites.store']
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



	def with_url(self, raw_url: str) -> ByRelationIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByRelationIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByRelationIdRequest(self.request_adapter, self.path_parameters)

	def from_term(self,
		site_id: str,
		store_id: str,
		group_id: str,
		set_id: str,
		term_id: str,
		term_id1: str,
		relation_id: str,
	) -> FromTermRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if store_id is None:
			raise TypeError("store_id cannot be null.")
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if set_id is None:
			raise TypeError("set_id cannot be null.")
		if term_id is None:
			raise TypeError("term_id cannot be null.")
		if term_id1 is None:
			raise TypeError("term_id1 cannot be null.")
		if relation_id is None:
			raise TypeError("relation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["store%2Did"] =  store_id
		path_parameters["group%2Did"] =  group_id
		path_parameters["set%2Did"] =  set_id
		path_parameters["term%2Did"] =  term_id
		path_parameters["term%2Did1"] =  term_id1
		path_parameters["relation%2Did"] =  relation_id

		from .from_term import FromTermRequest
		return FromTermRequest(self.request_adapter, path_parameters)

	def set(self,
		site_id: str,
		store_id: str,
		group_id: str,
		set_id: str,
		term_id: str,
		term_id1: str,
		relation_id: str,
	) -> SetRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if store_id is None:
			raise TypeError("store_id cannot be null.")
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if set_id is None:
			raise TypeError("set_id cannot be null.")
		if term_id is None:
			raise TypeError("term_id cannot be null.")
		if term_id1 is None:
			raise TypeError("term_id1 cannot be null.")
		if relation_id is None:
			raise TypeError("relation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["store%2Did"] =  store_id
		path_parameters["group%2Did"] =  group_id
		path_parameters["set%2Did"] =  set_id
		path_parameters["term%2Did"] =  term_id
		path_parameters["term%2Did1"] =  term_id1
		path_parameters["relation%2Did"] =  relation_id

		from .set import SetRequest
		return SetRequest(self.request_adapter, path_parameters)

	def to_term(self,
		site_id: str,
		store_id: str,
		group_id: str,
		set_id: str,
		term_id: str,
		term_id1: str,
		relation_id: str,
	) -> ToTermRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if store_id is None:
			raise TypeError("store_id cannot be null.")
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if set_id is None:
			raise TypeError("set_id cannot be null.")
		if term_id is None:
			raise TypeError("term_id cannot be null.")
		if term_id1 is None:
			raise TypeError("term_id1 cannot be null.")
		if relation_id is None:
			raise TypeError("relation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["store%2Did"] =  store_id
		path_parameters["group%2Did"] =  group_id
		path_parameters["set%2Did"] =  set_id
		path_parameters["term%2Did"] =  term_id
		path_parameters["term%2Did1"] =  term_id1
		path_parameters["relation%2Did"] =  relation_id

		from .to_term import ToTermRequest
		return ToTermRequest(self.request_adapter, path_parameters)

