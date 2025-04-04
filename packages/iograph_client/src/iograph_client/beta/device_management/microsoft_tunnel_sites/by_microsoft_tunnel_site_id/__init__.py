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
	from .microsoft_tunnel_servers import MicrosoftTunnelServersRequest
	from .microsoft_tunnel_configuration import MicrosoftTunnelConfigurationRequest
	from .request_upgrade import RequestUpgradeRequest
	from .....request_adapter import HttpxRequestAdapter
from iograph_models.beta.microsoft_tunnel_site import MicrosoftTunnelSite
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class ByMicrosoftTunnelSiteIdRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/microsoftTunnelSites/{microsoftTunnelSite%2Did}", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> MicrosoftTunnelSite:
		"""
		Get microsoftTunnelSites from deviceManagement
		Collection of MicrosoftTunnelSite settings associated with account.
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
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelSite, error_mapping)

	async def patch(
		self,
		body: MicrosoftTunnelSite,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> MicrosoftTunnelSite:
		"""
		Update the navigation property microsoftTunnelSites in deviceManagement
		
		"""
		tags = ['deviceManagement.microsoftTunnelSite']

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
		return await self.request_adapter.send_async(request_info, MicrosoftTunnelSite, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property microsoftTunnelSites for deviceManagement
		
		"""
		tags = ['deviceManagement.microsoftTunnelSite']
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



	def with_url(self, raw_url: str) -> ByMicrosoftTunnelSiteIdRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: ByMicrosoftTunnelSiteIdRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return ByMicrosoftTunnelSiteIdRequest(self.request_adapter, self.path_parameters)

	def request_upgrade(self,
		microsoftTunnelSite_id: str,
	) -> RequestUpgradeRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id

		from .request_upgrade import RequestUpgradeRequest
		return RequestUpgradeRequest(self.request_adapter, path_parameters)

	def microsoft_tunnel_configuration(self,
		microsoftTunnelSite_id: str,
	) -> MicrosoftTunnelConfigurationRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id

		from .microsoft_tunnel_configuration import MicrosoftTunnelConfigurationRequest
		return MicrosoftTunnelConfigurationRequest(self.request_adapter, path_parameters)

	def microsoft_tunnel_servers(self,
		microsoftTunnelSite_id: str,
	) -> MicrosoftTunnelServersRequest:
		if microsoftTunnelSite_id is None:
			raise TypeError("microsoftTunnelSite_id cannot be null.")

		path_parameters = get_path_parameters(self.path_parameters)
		path_parameters["microsoftTunnelSite%2Did"] =  microsoftTunnelSite_id

		from .microsoft_tunnel_servers import MicrosoftTunnelServersRequest
		return MicrosoftTunnelServersRequest(self.request_adapter, path_parameters)

