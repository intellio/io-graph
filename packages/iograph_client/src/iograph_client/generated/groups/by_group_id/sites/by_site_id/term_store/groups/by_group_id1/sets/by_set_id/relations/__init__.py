# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ............request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_relation_id import ByRelationIdRequest
	from ............request_adapter import HttpxRequestAdapter
from iograph_models.models.term_store_relation import TermStoreRelation
from iograph_models.models.term_store_relation_collection_response import TermStoreRelationCollectionResponse
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError


class RelationsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/termStore/groups/{group%2Did1}/sets/{set%2Did}/relations", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> TermStoreRelationCollectionResponse:
		"""
		Get relations from groups
		Indicates which terms have been pinned or reused directly under the set.
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
		return await self.request_adapter.send_async(request_info, TermStoreRelationCollectionResponse, error_mapping)

	async def post(
		self,
		body: TermStoreRelation,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> TermStoreRelation:
		"""
		Create new navigation property to relations for groups
		
		"""
		tags = ['groups.site']

		error_mapping: dict[str, type[BaseModel]] = {
			"XXX": ODataErrorsODataError,
		}

		request_info: RequestInformation = RequestInformation(
			method = Method.POST,
			url_template = self.url_template,
			path_parameters = self.path_parameters,
		)
		request_info.configure(request_configuration)
		request_info.headers.try_add("Accept", "application/json")
		request_info.set_content(body, "application/json")
		return await self.request_adapter.send_async(request_info, TermStoreRelation, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> RelationsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: RelationsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return RelationsRequest(self.request_adapter, self.path_parameters)

	def by_relation_id(self,
		group_id: str,
		site_id: str,
		group_id1: str,
		set_id: str,
		relation_id: str,
	) -> ByRelationIdRequest:
		if group_id is None:
			raise TypeError("group_id cannot be null.")
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if group_id1 is None:
			raise TypeError("group_id1 cannot be null.")
		if set_id is None:
			raise TypeError("set_id cannot be null.")
		if relation_id is None:
			raise TypeError("relation_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["group%2Did"] =  group_id
		path_parameters["site%2Did"] =  site_id
		path_parameters["group%2Did1"] =  group_id1
		path_parameters["set%2Did"] =  set_id
		path_parameters["relation%2Did"] =  relation_id

		from .by_relation_id import ByRelationIdRequest
		return ByRelationIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

