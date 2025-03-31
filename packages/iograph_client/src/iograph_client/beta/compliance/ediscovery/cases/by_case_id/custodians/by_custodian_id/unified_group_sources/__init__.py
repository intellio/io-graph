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
	from .by_unified_group_source_id import ByUnifiedGroupSourceIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.ediscovery_unified_group_source_collection_response import EdiscoveryUnifiedGroupSourceCollectionResponse
from iograph_models.beta.ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class UnifiedGroupSourcesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/custodians/{custodian%2Did}/unifiedGroupSources", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoveryUnifiedGroupSourceCollectionResponse:
		"""
		List unifiedGroupSources
		Get a list of the unifiedGroupSource objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-list-unifiedgroupsources?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryUnifiedGroupSourceCollectionResponse, error_mapping)

	async def post(
		self,
		body: EdiscoveryUnifiedGroupSource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoveryUnifiedGroupSource:
		"""
		Create unifiedGroupSource
		Create a new unifiedGroupSource object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-post-unifiedgroupsources?view=graph-rest-beta
		"""
		tags = ['compliance.ediscoveryroot']

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
		return await self.request_adapter.send_async(request_info, EdiscoveryUnifiedGroupSource, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> UnifiedGroupSourcesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: UnifiedGroupSourcesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return UnifiedGroupSourcesRequest(self.request_adapter, self.path_parameters)

	def by_unified_group_source_id(self,
		case_id: str,
		custodian_id: str,
		unifiedGroupSource_id: str,
	) -> ByUnifiedGroupSourceIdRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")
		if unifiedGroupSource_id is None:
			raise TypeError("unifiedGroupSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id
		path_parameters["unifiedGroupSource%2Did"] =  unifiedGroupSource_id

		from .by_unified_group_source_id import ByUnifiedGroupSourceIdRequest
		return ByUnifiedGroupSourceIdRequest(self.request_adapter, path_parameters)

	def count(self,
		case_id: str,
		custodian_id: str,
	) -> CountRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

