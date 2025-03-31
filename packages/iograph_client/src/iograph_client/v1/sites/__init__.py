# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .remove import RemoveRequest
	from .get_all_sites import GetAllSitesRequest
	from .delta import DeltaRequest
	from .add import AddRequest
	from .count import CountRequest
	from .by_site_id import BySiteIdRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.v1.site_collection_response import SiteCollectionResponse
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError


class SitesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SiteCollectionResponse:
		"""
		List sites
		List all available sites in an organization. Specific filter criteria and query options are also supported and described below: In addition, you can use a $search query against the /sites collection to find sites matching given keywords.
If you want to list all sites across all geographies, refer to getAllSites. For more guidance about building applications that use site discovery for scanning purposes, see Best practices for discovering files and detecting changes at scale.
		Find more info here: https://learn.microsoft.com/graph/api/site-list?view=graph-rest-1.0
		"""
		tags = ['sites.site']

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
		return await self.request_adapter.send_async(request_info, SiteCollectionResponse, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")

	def with_url(self, raw_url: str) -> SitesRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SitesRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SitesRequest(self.request_adapter, self.path_parameters)

	def by_site_id(self,
		site_id: str,
	) -> BySiteIdRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id

		from .by_site_id import BySiteIdRequest
		return BySiteIdRequest(self.request_adapter, path_parameters)

	@property
	def count(self,
	) -> CountRequest:
		from .count import CountRequest
		return CountRequest(self.request_adapter, self.path_parameters)

	@property
	def add(self,
	) -> AddRequest:
		from .add import AddRequest
		return AddRequest(self.request_adapter, self.path_parameters)

	@property
	def delta(self,
	) -> DeltaRequest:
		from .delta import DeltaRequest
		return DeltaRequest(self.request_adapter, self.path_parameters)

	@property
	def get_all_sites(self,
	) -> GetAllSitesRequest:
		from .get_all_sites import GetAllSitesRequest
		return GetAllSitesRequest(self.request_adapter, self.path_parameters)

	@property
	def remove(self,
	) -> RemoveRequest:
		from .remove import RemoveRequest
		return RemoveRequest(self.request_adapter, self.path_parameters)

