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
	from .by_connectivity_configuration_link_id import ByConnectivityConfigurationLinkIdRequest
	from ........request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_connectivity_configuration_link import NetworkaccessConnectivityConfigurationLink
from iograph_models.beta.networkaccess_connectivity_configuration_link_collection_response import NetworkaccessConnectivityConfigurationLinkCollectionResponse
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class LinksRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}/connectivityConfiguration/links", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessConnectivityConfigurationLinkCollectionResponse:
		"""
		Get links from networkAccess
		List of connectivity configurations for deviceLink objects.
		"""
		tags = ['networkAccess.connectivity']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessConnectivityConfigurationLinkCollectionResponse, error_mapping)

	async def post(
		self,
		body: NetworkaccessConnectivityConfigurationLink,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessConnectivityConfigurationLink:
		"""
		Create new navigation property to links for networkAccess
		
		"""
		tags = ['networkAccess.connectivity']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessConnectivityConfigurationLink, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> LinksRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: LinksRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return LinksRequest(self.request_adapter, self.path_parameters)

	def by_connectivity_configuration_link_id(self,
		branchSite_id: str,
		connectivityConfigurationLink_id: str,
	) -> ByConnectivityConfigurationLinkIdRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")
		if connectivityConfigurationLink_id is None:
			raise TypeError("connectivityConfigurationLink_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id
		path_parameters["connectivityConfigurationLink%2Did"] =  connectivityConfigurationLink_id

		from .by_connectivity_configuration_link_id import ByConnectivityConfigurationLinkIdRequest
		return ByConnectivityConfigurationLinkIdRequest(self.request_adapter, path_parameters)

	def count(self,
		branchSite_id: str,
	) -> CountRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

