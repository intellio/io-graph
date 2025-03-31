# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ..........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .sets import SetsRequest
	from ..........request_adapter import HttpxRequestAdapter
from iograph_models.v1.term_store_group import TermStoreGroup
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class ByGroupId1Request(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/termStores/{store%2Did}/groups/{group%2Did1}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermStoreGroup:
		"""
		Get groups from groups
		Collection of all groups available in the term store.
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, TermStoreGroup, error_mapping)

	async def patch(
		self,
		body: TermStoreGroup,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermStoreGroup:
		"""
		Update the navigation property groups in groups
		
		"""
		tags = ['groups.site']

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
		return await self.request_adapter.send_async(request_info, TermStoreGroup, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property groups for groups
		
		"""
		tags = ['groups.site']
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



	def with_url(self, raw_url: str) -> ByGroupId1Request:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByGroupId1Request
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByGroupId1Request(self.request_adapter, self.path_parameters)

	def sets(self,
		group_id: str,
		site_id: str,
		store_id: str,
		group_id1: str,
	) -> SetsRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if store_id is None:
			raise TypeError("store_id cannot be null.")
		if group_id1 is None:
			raise TypeError("group_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["store%2Did"] =  store_id
		path_parameters["group%2Did1"] =  group_id1

		from .sets import SetsRequest
		return SetsRequest(self.request_adapter, path_parameters)

