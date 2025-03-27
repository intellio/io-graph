# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ........request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_browser_site_id import ByBrowserSiteIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.browser_site import BrowserSite
from iograph_models.beta.browser_site_collection_response import BrowserSiteCollectionResponse


class SitesRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/admin/edge/internetExplorerMode/siteLists/{browserSiteList%2Did}/sites", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> BrowserSiteCollectionResponse:
		"""
		List browserSites
		Get a list of the browserSite objects and their properties.
		Find more info here: https://learn.microsoft.com/graph/api/browsersitelist-list-sites?view=graph-rest-beta
		"""
		tags = ['admin.edge']

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
		return await self.request_adapter.send_async(request_info, BrowserSiteCollectionResponse, error_mapping)

	async def post(
		self,
		body: BrowserSite,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> BrowserSite:
		"""
		Create browserSite
		Create a new browserSite object in a browserSiteList.
		Find more info here: https://learn.microsoft.com/graph/api/browsersitelist-post-sites?view=graph-rest-beta
		"""
		tags = ['admin.edge']

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
		return await self.request_adapter.send_async(request_info, BrowserSite, error_mapping)

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

	def by_browser_site_id(self,
		browserSiteList_id: str,
		browserSite_id: str,
	) -> ByBrowserSiteIdRequest:
		if browserSiteList_id is None:
			raise TypeError("browserSiteList_id cannot be null.")
		if browserSite_id is None:
			raise TypeError("browserSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["browserSiteList%2Did"] =  browserSiteList_id
		path_parameters["browserSite%2Did"] =  browserSite_id

		from .by_browser_site_id import ByBrowserSiteIdRequest
		return ByBrowserSiteIdRequest(self.request_adapter, path_parameters)

	def count(self,
		browserSiteList_id: str,
	) -> CountRequest:
		if browserSiteList_id is None:
			raise TypeError("browserSiteList_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["browserSiteList%2Did"] =  browserSiteList_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

