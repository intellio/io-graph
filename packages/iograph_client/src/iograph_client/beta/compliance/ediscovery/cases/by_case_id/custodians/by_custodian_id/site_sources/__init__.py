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
	from .by_site_source_id import BySiteSourceIdRequest
	from .........request_adapter import HttpxRequestAdapter
from iograph_models.beta.ediscovery_site_source import EdiscoverySiteSource
from iograph_models.beta.ediscovery_site_source_collection_response import EdiscoverySiteSourceCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SiteSourcesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/custodians/{custodian%2Did}/siteSources", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> EdiscoverySiteSourceCollectionResponse:
		"""
		List custodian siteSources
		Get a list of siteSource objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-list-sitesources?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EdiscoverySiteSourceCollectionResponse, error_mapping)

	async def post(
		self,
		body: EdiscoverySiteSource,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> EdiscoverySiteSource:
		"""
		Create custodian siteSource
		Create a new custodian siteSource object.
		Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-post-sitesources?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, EdiscoverySiteSource, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> SiteSourcesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SiteSourcesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SiteSourcesRequest(self.request_adapter, self.path_parameters)

	def by_site_source_id(self,
		case_id: str,
		custodian_id: str,
		siteSource_id: str,
	) -> BySiteSourceIdRequest:
		if case_id is None:
			raise TypeError("case_id cannot be null.")
		if custodian_id is None:
			raise TypeError("custodian_id cannot be null.")
		if siteSource_id is None:
			raise TypeError("siteSource_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["case%2Did"] =  case_id
		path_parameters["custodian%2Did"] =  custodian_id
		path_parameters["siteSource%2Did"] =  siteSource_id

		from .by_site_source_id import BySiteSourceIdRequest
		return BySiteSourceIdRequest(self.request_adapter, path_parameters)

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

