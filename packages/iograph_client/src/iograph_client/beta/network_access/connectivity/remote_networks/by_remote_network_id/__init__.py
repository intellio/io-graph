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
	from .forwarding_profiles import ForwardingProfilesRequest
	from .device_links import DeviceLinksRequest
	from .connectivity_configuration import ConnectivityConfigurationRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_remote_network import NetworkaccessRemoteNetwork
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByRemoteNetworkIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/connectivity/remoteNetworks/{remoteNetwork%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessRemoteNetwork:
		"""
		Get remoteNetworks from networkAccess
		The locations, such as branches, that are connected to Global Secure Access services through an IPsec tunnel.
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
		return await self.request_adapter.send_async(request_info, NetworkaccessRemoteNetwork, error_mapping)

	async def patch(
		self,
		body: NetworkaccessRemoteNetwork,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessRemoteNetwork:
		"""
		Update the navigation property remoteNetworks in networkAccess
		
		"""
		tags = ['networkAccess.connectivity']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessRemoteNetwork, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property remoteNetworks for networkAccess
		
		"""
		tags = ['networkAccess.connectivity']
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



	def with_url(self, raw_url: str) -> ByRemoteNetworkIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByRemoteNetworkIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByRemoteNetworkIdRequest(self.request_adapter, self.path_parameters)

	def connectivity_configuration(self,
		remoteNetwork_id: str,
	) -> ConnectivityConfigurationRequest:
		if remoteNetwork_id is None:
			raise TypeError("remoteNetwork_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["remoteNetwork%2Did"] =  remoteNetwork_id

		from .connectivity_configuration import ConnectivityConfigurationRequest
		return ConnectivityConfigurationRequest(self.request_adapter, path_parameters)

	def device_links(self,
		remoteNetwork_id: str,
	) -> DeviceLinksRequest:
		if remoteNetwork_id is None:
			raise TypeError("remoteNetwork_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["remoteNetwork%2Did"] =  remoteNetwork_id

		from .device_links import DeviceLinksRequest
		return DeviceLinksRequest(self.request_adapter, path_parameters)

	def forwarding_profiles(self,
		remoteNetwork_id: str,
	) -> ForwardingProfilesRequest:
		if remoteNetwork_id is None:
			raise TypeError("remoteNetwork_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["remoteNetwork%2Did"] =  remoteNetwork_id

		from .forwarding_profiles import ForwardingProfilesRequest
		return ForwardingProfilesRequest(self.request_adapter, path_parameters)

