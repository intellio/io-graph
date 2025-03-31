# Auto-generated client

from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from .......request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .count import CountRequest
	from .by_device_link_id import ByDeviceLinkIdRequest
	from .......request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_device_link_collection_response import NetworkaccessDeviceLinkCollectionResponse
from iograph_models.beta.networkaccess_device_link import NetworkaccessDeviceLink
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class DeviceLinksRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/branches/{branchSite%2Did}/deviceLinks", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessDeviceLinkCollectionResponse:
		"""
		List deviceLinks (deprecated)
		Retrieve a list of device links associated with a specific branch.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-list-devicelinks?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, NetworkaccessDeviceLinkCollectionResponse, error_mapping)

	async def post(
		self,
		body: NetworkaccessDeviceLink,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessDeviceLink:
		"""
		Create deviceLink (deprecated)
		Create a branch site with associated device links.
		Find more info here: https://learn.microsoft.com/graph/api/networkaccess-branchsite-post-devicelinks?view=graph-rest-beta
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
		return await self.request_adapter.send_async(request_info, NetworkaccessDeviceLink, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceLinksRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceLinksRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceLinksRequest(self.request_adapter, self.path_parameters)

	def by_device_link_id(self,
		branchSite_id: str,
		deviceLink_id: str,
	) -> ByDeviceLinkIdRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")
		if deviceLink_id is None:
			raise TypeError("deviceLink_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id
		path_parameters["deviceLink%2Did"] =  deviceLink_id

		from .by_device_link_id import ByDeviceLinkIdRequest
		return ByDeviceLinkIdRequest(self.request_adapter, path_parameters)

	def count(self,
		branchSite_id: str,
	) -> CountRequest:
		if branchSite_id is None:
			raise TypeError("branchSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["branchSite%2Did"] =  branchSite_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

