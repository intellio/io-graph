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
	from .user_settings import UserSettingsRequest
	from .provisioning_policies import ProvisioningPoliciesRequest
	from .on_premises_connections import OnPremisesConnectionsRequest
	from .gallery_images import GalleryImagesRequest
	from .device_images import DeviceImagesRequest
	from .cloud_p_cs import CloudPCsRequest
	from .audit_events import AuditEventsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.v1.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.v1.virtual_endpoint import VirtualEndpoint


class VirtualEndpointRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEndpoint:
		"""
		Get virtualEndpoint from deviceManagement
		Virtual endpoint
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, VirtualEndpoint, error_mapping)

	async def patch(
		self,
		body: VirtualEndpoint,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> VirtualEndpoint:
		"""
		Update the navigation property virtualEndpoint in deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']

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
		return await self.request_adapter.send_async(request_info, VirtualEndpoint, error_mapping)

	async def delete(
		self,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> None:
		"""
		Delete navigation property virtualEndpoint for deviceManagement
		
		"""
		tags = ['deviceManagement.virtualEndpoint']
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



	def with_url(self, raw_url: str) -> VirtualEndpointRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: VirtualEndpointRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return VirtualEndpointRequest(self.request_adapter, self.path_parameters)

	@property
	def audit_events(self,
	) -> AuditEventsRequest:
		from .audit_events import AuditEventsRequest
		return AuditEventsRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_p_cs(self,
	) -> CloudPCsRequest:
		from .cloud_p_cs import CloudPCsRequest
		return CloudPCsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_images(self,
	) -> DeviceImagesRequest:
		from .device_images import DeviceImagesRequest
		return DeviceImagesRequest(self.request_adapter, self.path_parameters)

	@property
	def gallery_images(self,
	) -> GalleryImagesRequest:
		from .gallery_images import GalleryImagesRequest
		return GalleryImagesRequest(self.request_adapter, self.path_parameters)

	@property
	def on_premises_connections(self,
	) -> OnPremisesConnectionsRequest:
		from .on_premises_connections import OnPremisesConnectionsRequest
		return OnPremisesConnectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def provisioning_policies(self,
	) -> ProvisioningPoliciesRequest:
		from .provisioning_policies import ProvisioningPoliciesRequest
		return ProvisioningPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def user_settings(self,
	) -> UserSettingsRequest:
		from .user_settings import UserSettingsRequest
		return UserSettingsRequest(self.request_adapter, self.path_parameters)

