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
	from .supported_regions import SupportedRegionsRequest
	from .snapshots import SnapshotsRequest
	from .service_plans import ServicePlansRequest
	from .reports import ReportsRequest
	from .provisioning_policies import ProvisioningPoliciesRequest
	from .organization_settings import OrganizationSettingsRequest
	from .on_premises_connections import OnPremisesConnectionsRequest
	from .retrieve_tenant_encryption_setting import RetrieveTenantEncryptionSettingRequest
	from .retrieve_scoped_permissions import RetrieveScopedPermissionsRequest
	from .get_effective_permissions import GetEffectivePermissionsRequest
	from .gallery_images import GalleryImagesRequest
	from .front_line_service_plans import FrontLineServicePlansRequest
	from .external_partner_settings import ExternalPartnerSettingsRequest
	from .device_images import DeviceImagesRequest
	from .cross_cloud_government_organization_mapping import CrossCloudGovernmentOrganizationMappingRequest
	from .cloud_p_cs import CloudPCsRequest
	from .bulk_actions import BulkActionsRequest
	from .audit_events import AuditEventsRequest
	from ....request_adapter import HttpxRequestAdapter
from iograph_models.beta.virtual_endpoint import VirtualEndpoint
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError


class VirtualEndpointRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> VirtualEndpoint:
		"""
		Get virtualEndpoint from deviceManagement
		
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
	def bulk_actions(self,
	) -> BulkActionsRequest:
		from .bulk_actions import BulkActionsRequest
		return BulkActionsRequest(self.request_adapter, self.path_parameters)

	@property
	def cloud_p_cs(self,
	) -> CloudPCsRequest:
		from .cloud_p_cs import CloudPCsRequest
		return CloudPCsRequest(self.request_adapter, self.path_parameters)

	@property
	def cross_cloud_government_organization_mapping(self,
	) -> CrossCloudGovernmentOrganizationMappingRequest:
		from .cross_cloud_government_organization_mapping import CrossCloudGovernmentOrganizationMappingRequest
		return CrossCloudGovernmentOrganizationMappingRequest(self.request_adapter, self.path_parameters)

	@property
	def device_images(self,
	) -> DeviceImagesRequest:
		from .device_images import DeviceImagesRequest
		return DeviceImagesRequest(self.request_adapter, self.path_parameters)

	@property
	def external_partner_settings(self,
	) -> ExternalPartnerSettingsRequest:
		from .external_partner_settings import ExternalPartnerSettingsRequest
		return ExternalPartnerSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def front_line_service_plans(self,
	) -> FrontLineServicePlansRequest:
		from .front_line_service_plans import FrontLineServicePlansRequest
		return FrontLineServicePlansRequest(self.request_adapter, self.path_parameters)

	@property
	def gallery_images(self,
	) -> GalleryImagesRequest:
		from .gallery_images import GalleryImagesRequest
		return GalleryImagesRequest(self.request_adapter, self.path_parameters)

	@property
	def get_effective_permissions(self,
	) -> GetEffectivePermissionsRequest:
		from .get_effective_permissions import GetEffectivePermissionsRequest
		return GetEffectivePermissionsRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_scoped_permissions(self,
	) -> RetrieveScopedPermissionsRequest:
		from .retrieve_scoped_permissions import RetrieveScopedPermissionsRequest
		return RetrieveScopedPermissionsRequest(self.request_adapter, self.path_parameters)

	@property
	def retrieve_tenant_encryption_setting(self,
	) -> RetrieveTenantEncryptionSettingRequest:
		from .retrieve_tenant_encryption_setting import RetrieveTenantEncryptionSettingRequest
		return RetrieveTenantEncryptionSettingRequest(self.request_adapter, self.path_parameters)

	@property
	def on_premises_connections(self,
	) -> OnPremisesConnectionsRequest:
		from .on_premises_connections import OnPremisesConnectionsRequest
		return OnPremisesConnectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def organization_settings(self,
	) -> OrganizationSettingsRequest:
		from .organization_settings import OrganizationSettingsRequest
		return OrganizationSettingsRequest(self.request_adapter, self.path_parameters)

	@property
	def provisioning_policies(self,
	) -> ProvisioningPoliciesRequest:
		from .provisioning_policies import ProvisioningPoliciesRequest
		return ProvisioningPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def reports(self,
	) -> ReportsRequest:
		from .reports import ReportsRequest
		return ReportsRequest(self.request_adapter, self.path_parameters)

	@property
	def service_plans(self,
	) -> ServicePlansRequest:
		from .service_plans import ServicePlansRequest
		return ServicePlansRequest(self.request_adapter, self.path_parameters)

	@property
	def snapshots(self,
	) -> SnapshotsRequest:
		from .snapshots import SnapshotsRequest
		return SnapshotsRequest(self.request_adapter, self.path_parameters)

	@property
	def supported_regions(self,
	) -> SupportedRegionsRequest:
		from .supported_regions import SupportedRegionsRequest
		return SupportedRegionsRequest(self.request_adapter, self.path_parameters)

	@property
	def user_settings(self,
	) -> UserSettingsRequest:
		from .user_settings import UserSettingsRequest
		return UserSettingsRequest(self.request_adapter, self.path_parameters)

