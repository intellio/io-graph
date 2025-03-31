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
	from .count import CountRequest
	from .by_microsoft_tunnel_server_id import ByMicrosoftTunnelServerIdRequest
	from ......request_adapter import HttpxRequestAdapter
from iograph_models.beta.microsoft_tunnel_server_collection_response import MicrosoftTunnelServerCollectionResponse
from iograph_models.beta.microsoft_tunnel_server import MicrosoftTunnelServer
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class MicrosoftTunnelServersRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/microsoftTunnelSites/{microsoftTunnelSite%2Did}/microsoftTunnelServers", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MicrosoftTunnelServerCollectionResponse:
		"""
		Get microsoftTunnelServers from deviceManagement
		A list of MicrosoftTunnelServers that are registered to this MicrosoftTunnelSite
		"""
		tags = ['deviceManagement.microsoftTunnelSite']

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
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelServerCollectionResponse, error_mapping)

	async def post(
		self,
		body: MicrosoftTunnelServer,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MicrosoftTunnelServer:
		"""
		Create new navigation property to microsoftTunnelServers for deviceManagement
		
		"""
		tags = ['deviceManagement.microsoftTunnelSite']

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
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelServer, error_mapping)

	class GetQueryParams(BaseModel):
		top: int = Field(default=None,serialization_alias="%24top")
		skip: int = Field(default=None,serialization_alias="%24skip")
		search: str = Field(default=None,serialization_alias="%24search")
		filter: str = Field(default=None,serialization_alias="%24filter")
		count: bool = Field(default=None,serialization_alias="%24count")
		orderby: list[str] = Field(default=None,serialization_alias="%24orderby")
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> MicrosoftTunnelServersRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: MicrosoftTunnelServersRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return MicrosoftTunnelServersRequest(self.request_adapter, self.path_parameters)

	def by_microsoft_tunnel_server_id(self,
		microsoftTunnelSite_id: str,
		microsoftTunnelServer_id: str,
	) -> ByMicrosoftTunnelServerIdRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")
		if microsoftTunnelServer_id is None:
			raise TypeError("microsoftTunnelServer_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id
		path_parameters["microsoftTunnelServer%2Did"] =  microsoftTunnelServer_id

		from .by_microsoft_tunnel_server_id import ByMicrosoftTunnelServerIdRequest
		return ByMicrosoftTunnelServerIdRequest(self.request_adapter, path_parameters)

	def count(self,
		microsoftTunnelSite_id: str,
	) -> CountRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id

		from .count import CountRequest
		return CountRequest(self.request_adapter, path_parameters)

