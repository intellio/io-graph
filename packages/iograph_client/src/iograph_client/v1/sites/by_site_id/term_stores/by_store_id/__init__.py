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
	from .sets import SetsRequest
	from .groups import GroupsRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.v1.term_store_store import TermStoreStore
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByStoreIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/termStores/{store%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermStoreStore:
		"""
		Get termStores from sites
		The collection of termStores under this site.
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
		return await self.request_adapter.send_async(request_info, TermStoreStore, error_mapping)

	async def patch(
		self,
		body: TermStoreStore,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermStoreStore:
		"""
		Update the navigation property termStores in sites
		
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
		return await self.request_adapter.send_async(request_info, TermStoreStore, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property termStores for sites
		
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



	def with_url(self, raw_url: str) -> ByStoreIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByStoreIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByStoreIdRequest(self.request_adapter, self.path_parameters)

	def groups(self,
		site_id: str,
		store_id: str,
	) -> GroupsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if store_id is None:
			raise TypeError("store_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["store%2Did"] =  store_id

		from .groups import GroupsRequest
		return GroupsRequest(self.request_adapter, path_parameters)

	def sets(self,
		site_id: str,
		store_id: str,
	) -> SetsRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if store_id is None:
			raise TypeError("store_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["store%2Did"] =  store_id

		from .sets import SetsRequest
		return SetsRequest(self.request_adapter, path_parameters)

