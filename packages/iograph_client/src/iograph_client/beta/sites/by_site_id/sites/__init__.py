# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_site_id1 import BySiteId1Request
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.site_collection_response import SiteCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class SitesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/sites", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> SiteCollectionResponse:
		"""
		List subsites for a site
		Get a collection of subsites defined for a site.
		Find more info here: https://learn.microsoft.com/graph/api/site-list-subsites?view=graph-rest-beta
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

	def by_site_id1(self,
		site_id: str,
		site_id1: str,
	) -> BySiteId1Request:
		if site_id is None:
			raise TypeError("site_id cannot be null.")
		if site_id1 is None:
			raise TypeError("site_id1 cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id
		path_parameters["site%2Did1"] =  site_id1

		from .by_site_id1 import BySiteId1Request
		return BySiteId1Request(self.request_adapter, path_parameters)

	def count(self,
		site_id: str,
	) -> CountRequest:
		if site_id is None:
			raise TypeError("site_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["site%2Did"] =  site_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

