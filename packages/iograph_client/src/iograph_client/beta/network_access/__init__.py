# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ...request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .tenant_status import TenantStatusRequest
	from .settings import SettingsRequest
	from .reports import ReportsRequest
	from .networkaccess_onboard import NetworkaccessOnboardRequest
	from .logs import LogsRequest
	from .forwarding_profiles import ForwardingProfilesRequest
	from .forwarding_policies import ForwardingPoliciesRequest
	from .filtering_profiles import FilteringProfilesRequest
	from .filtering_policies import FilteringPoliciesRequest
	from .connectivity import ConnectivityRequest
	from .alerts import AlertsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.networkaccess_network_access_root import NetworkaccessNetworkAccessRoot
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class NetworkAccessRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessNetworkAccessRoot:
		"""
		Get networkAccess
		
		"""
		tags = ['networkAccess.networkAccessRoot']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessNetworkAccessRoot, error_mapping)

	async def patch(
		self,
		body: NetworkaccessNetworkAccessRoot,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessNetworkAccessRoot:
		"""
		Update networkAccess
		
		"""
		tags = ['networkAccess.networkAccessRoot']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessNetworkAccessRoot, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> NetworkAccessRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: NetworkAccessRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return NetworkAccessRequest(self.request_adapter, self.path_parameters)

	@property
	def alerts(self,
	) -> AlertsRequest:
		from .alerts import AlertsRequest
		return AlertsRequest(self.request_adapter, self.path_parameters)

	@property
	def connectivity(self,
	) -> ConnectivityRequest:
		from .connectivity import ConnectivityRequest
		return ConnectivityRequest(self.request_adapter, self.path_parameters)

	@property
	def filtering_policies(self,
	) -> FilteringPoliciesRequest:
		from .filtering_policies import FilteringPoliciesRequest
		return FilteringPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def filtering_profiles(self,
	) -> FilteringProfilesRequest:
		from .filtering_profiles import FilteringProfilesRequest
		return FilteringProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def forwarding_policies(self,
	) -> ForwardingPoliciesRequest:
		from .forwarding_policies import ForwardingPoliciesRequest
		return ForwardingPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def forwarding_profiles(self,
	) -> ForwardingProfilesRequest:
		from .forwarding_profiles import ForwardingProfilesRequest
		return ForwardingProfilesRequest(self.request_adapter, self.path_parameters)

	@property
	def logs(self,
	) -> LogsRequest:
		from .logs import LogsRequest
		return LogsRequest(self.request_adapter, self.path_parameters)

	@property
	def networkaccess_onboard(self,
	) -> NetworkaccessOnboardRequest:
		from .networkaccess_onboard import NetworkaccessOnboardRequest
		return NetworkaccessOnboardRequest(self.request_adapter, self.path_parameters)

	@property
	def reports(self,
	) -> ReportsRequest:
		from .reports import ReportsRequest
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def settings(self,
	) -> SettingsRequest:
		from .settings import SettingsRequest
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def tenant_status(self,
	) -> TenantStatusRequest:
		from .tenant_status import TenantStatusRequest
		return TenantStatusRequest(self.request_adapter, self.path_parameters)

