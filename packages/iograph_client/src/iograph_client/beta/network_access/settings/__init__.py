# Auto-generated client

from __future__ import annotations
from kiota_abstractions.method import Method
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from ....request_information import RequestInformation
from pydantic import BaseModel, Field
from typing import Union, Any, Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from .forwarding_options import ForwardingOptionsRequest
	from .enriched_audit_logs import EnrichedAuditLogsRequest
	from .cross_tenant_access import CrossTenantAccessRequest
	from .conditional_access import ConditionalAccessRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.networkaccess_settings import NetworkaccessSettings


class SettingsRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/networkAccess/settings", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> NetworkaccessSettings:
		"""
		Get settings from networkAccess
		Global Secure Access settings.
		"""
		tags = ['networkAccess.settings']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessSettings, error_mapping)

	async def patch(
		self,
		body: NetworkaccessSettings,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> NetworkaccessSettings:
		"""
		Update the navigation property settings in networkAccess
		
		"""
		tags = ['networkAccess.settings']

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
		return await self.request_adapter.send_async(request_info, NetworkaccessSettings, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property settings for networkAccess
		
		"""
		tags = ['networkAccess.settings']
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



	def with_url(self, raw_url: str) -> SettingsRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: SettingsRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return SettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def conditional_access(self,
	) -> ConditionalAccessRequest:
		from .conditional_access import ConditionalAccessRequest
		return ConditionalAccessRequest(self.request_adapter, self.path_parameters)

	@property
	def cross_tenant_access(self,
	) -> CrossTenantAccessRequest:
		from .cross_tenant_access import CrossTenantAccessRequest
		return CrossTenantAccessRequest(self.request_adapter, self.path_parameters)

	@property
	def enriched_audit_logs(self,
	) -> EnrichedAuditLogsRequest:
		from .enriched_audit_logs import EnrichedAuditLogsRequest
		return EnrichedAuditLogsRequest(self.request_adapter, self.path_parameters)

	@property
	def forwarding_options(self,
	) -> ForwardingOptionsRequest:
		from .forwarding_options import ForwardingOptionsRequest
		return ForwardingOptionsRequest(self.request_adapter, self.path_parameters)

