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
	from .windows_management_app import WindowsManagementAppRequest
	from .windows_managed_app_protections import WindowsManagedAppProtectionsRequest
	from .windows_information_protection_wipe_actions import WindowsInformationProtectionWipeActionsRequest
	from .windows_information_protection_policies import WindowsInformationProtectionPoliciesRequest
	from .windows_information_protection_device_registrations import WindowsInformationProtectionDeviceRegistrationsRequest
	from .wdac_supplemental_policies import WdacSupplementalPoliciesRequest
	from .vpp_tokens import VppTokensRequest
	from .targeted_managed_app_configurations import TargetedManagedAppConfigurationsRequest
	from .symantec_code_signing_certificate import SymantecCodeSigningCertificateRequest
	from .policy_sets import PolicySetsRequest
	from .mobile_apps import MobileAppsRequest
	from .mobile_app_relationships import MobileAppRelationshipsRequest
	from .mobile_app_configurations import MobileAppConfigurationsRequest
	from .mobile_app_categories import MobileAppCategoriesRequest
	from .mobile_app_catalog_packages import MobileAppCatalogPackagesRequest
	from .sync_microsoft_store_for_business_apps import SyncMicrosoftStoreForBusinessAppsRequest
	from .mdm_windows_information_protection_policies import MdmWindowsInformationProtectionPoliciesRequest
	from .managed_e_books import ManagedEBooksRequest
	from .managed_e_book_categories import ManagedEBookCategoriesRequest
	from .managed_app_statuses import ManagedAppStatusesRequest
	from .managed_app_registrations import ManagedAppRegistrationsRequest
	from .managed_app_policies import ManagedAppPoliciesRequest
	from .ios_managed_app_protections import IosManagedAppProtectionsRequest
	from .ios_lob_app_provisioning_configurations import IosLobAppProvisioningConfigurationsRequest
	from .enterprise_code_signing_certificates import EnterpriseCodeSigningCertificatesRequest
	from .device_app_management_tasks import DeviceAppManagementTasksRequest
	from .default_managed_app_protections import DefaultManagedAppProtectionsRequest
	from .android_managed_app_protections import AndroidManagedAppProtectionsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.beta.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.beta.device_app_management import DeviceAppManagement


class DeviceAppManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceAppManagement:
		"""
		Get deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.deviceAppManagement']

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
		return await self.request_adapter.send_async(request_info, DeviceAppManagement, error_mapping)

	async def patch(
		self,
		body: DeviceAppManagement,
		request_configuration: Optional[RequestConfiguration[BaseModel]] = None,
	) -> DeviceAppManagement:
		"""
		Update deviceAppManagement
		
		"""
		tags = ['deviceAppManagement.deviceAppManagement']

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
		return await self.request_adapter.send_async(request_info, DeviceAppManagement, error_mapping)

	class GetQueryParams(BaseModel):
		select: list[str] = Field(default=None,serialization_alias="%24select")
		expand: list[str] = Field(default=None,serialization_alias="%24expand")


	def with_url(self, raw_url: str) -> DeviceAppManagementRequest:
		"""
		Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
		param raw_url: The raw URL to use for the request builder.
		Returns: DeviceAppManagementRequest
		"""
		if raw_url is None:
			raise TypeError("raw_url cannot be None.")
		return DeviceAppManagementRequest(self.request_adapter, self.path_parameters)

	@property
	def android_managed_app_protections(self,
	) -> AndroidManagedAppProtectionsRequest:
		from .android_managed_app_protections import AndroidManagedAppProtectionsRequest
		return AndroidManagedAppProtectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def default_managed_app_protections(self,
	) -> DefaultManagedAppProtectionsRequest:
		from .default_managed_app_protections import DefaultManagedAppProtectionsRequest
		return DefaultManagedAppProtectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def device_app_management_tasks(self,
	) -> DeviceAppManagementTasksRequest:
		from .device_app_management_tasks import DeviceAppManagementTasksRequest
		return DeviceAppManagementTasksRequest(self.request_adapter, self.path_parameters)

	@property
	def enterprise_code_signing_certificates(self,
	) -> EnterpriseCodeSigningCertificatesRequest:
		from .enterprise_code_signing_certificates import EnterpriseCodeSigningCertificatesRequest
		return EnterpriseCodeSigningCertificatesRequest(self.request_adapter, self.path_parameters)

	@property
	def ios_lob_app_provisioning_configurations(self,
	) -> IosLobAppProvisioningConfigurationsRequest:
		from .ios_lob_app_provisioning_configurations import IosLobAppProvisioningConfigurationsRequest
		return IosLobAppProvisioningConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def ios_managed_app_protections(self,
	) -> IosManagedAppProtectionsRequest:
		from .ios_managed_app_protections import IosManagedAppProtectionsRequest
		return IosManagedAppProtectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_app_policies(self,
	) -> ManagedAppPoliciesRequest:
		from .managed_app_policies import ManagedAppPoliciesRequest
		return ManagedAppPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_app_registrations(self,
	) -> ManagedAppRegistrationsRequest:
		from .managed_app_registrations import ManagedAppRegistrationsRequest
		return ManagedAppRegistrationsRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_app_statuses(self,
	) -> ManagedAppStatusesRequest:
		from .managed_app_statuses import ManagedAppStatusesRequest
		return ManagedAppStatusesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_e_book_categories(self,
	) -> ManagedEBookCategoriesRequest:
		from .managed_e_book_categories import ManagedEBookCategoriesRequest
		return ManagedEBookCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def managed_e_books(self,
	) -> ManagedEBooksRequest:
		from .managed_e_books import ManagedEBooksRequest
		return ManagedEBooksRequest(self.request_adapter, self.path_parameters)

	@property
	def mdm_windows_information_protection_policies(self,
	) -> MdmWindowsInformationProtectionPoliciesRequest:
		from .mdm_windows_information_protection_policies import MdmWindowsInformationProtectionPoliciesRequest
		return MdmWindowsInformationProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def sync_microsoft_store_for_business_apps(self,
	) -> SyncMicrosoftStoreForBusinessAppsRequest:
		from .sync_microsoft_store_for_business_apps import SyncMicrosoftStoreForBusinessAppsRequest
		return SyncMicrosoftStoreForBusinessAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_app_catalog_packages(self,
	) -> MobileAppCatalogPackagesRequest:
		from .mobile_app_catalog_packages import MobileAppCatalogPackagesRequest
		return MobileAppCatalogPackagesRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_app_categories(self,
	) -> MobileAppCategoriesRequest:
		from .mobile_app_categories import MobileAppCategoriesRequest
		return MobileAppCategoriesRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_app_configurations(self,
	) -> MobileAppConfigurationsRequest:
		from .mobile_app_configurations import MobileAppConfigurationsRequest
		return MobileAppConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_app_relationships(self,
	) -> MobileAppRelationshipsRequest:
		from .mobile_app_relationships import MobileAppRelationshipsRequest
		return MobileAppRelationshipsRequest(self.request_adapter, self.path_parameters)

	@property
	def mobile_apps(self,
	) -> MobileAppsRequest:
		from .mobile_apps import MobileAppsRequest
		return MobileAppsRequest(self.request_adapter, self.path_parameters)

	@property
	def policy_sets(self,
	) -> PolicySetsRequest:
		from .policy_sets import PolicySetsRequest
		return PolicySetsRequest(self.request_adapter, self.path_parameters)

	@property
	def symantec_code_signing_certificate(self,
	) -> SymantecCodeSigningCertificateRequest:
		from .symantec_code_signing_certificate import SymantecCodeSigningCertificateRequest
		return SymantecCodeSigningCertificateRequest(self.request_adapter, self.path_parameters)

	@property
	def targeted_managed_app_configurations(self,
	) -> TargetedManagedAppConfigurationsRequest:
		from .targeted_managed_app_configurations import TargetedManagedAppConfigurationsRequest
		return TargetedManagedAppConfigurationsRequest(self.request_adapter, self.path_parameters)

	@property
	def vpp_tokens(self,
	) -> VppTokensRequest:
		from .vpp_tokens import VppTokensRequest
		return VppTokensRequest(self.request_adapter, self.path_parameters)

	@property
	def wdac_supplemental_policies(self,
	) -> WdacSupplementalPoliciesRequest:
		from .wdac_supplemental_policies import WdacSupplementalPoliciesRequest
		return WdacSupplementalPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_information_protection_device_registrations(self,
	) -> WindowsInformationProtectionDeviceRegistrationsRequest:
		from .windows_information_protection_device_registrations import WindowsInformationProtectionDeviceRegistrationsRequest
		return WindowsInformationProtectionDeviceRegistrationsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_information_protection_policies(self,
	) -> WindowsInformationProtectionPoliciesRequest:
		from .windows_information_protection_policies import WindowsInformationProtectionPoliciesRequest
		return WindowsInformationProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_information_protection_wipe_actions(self,
	) -> WindowsInformationProtectionWipeActionsRequest:
		from .windows_information_protection_wipe_actions import WindowsInformationProtectionWipeActionsRequest
		return WindowsInformationProtectionWipeActionsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_managed_app_protections(self,
	) -> WindowsManagedAppProtectionsRequest:
		from .windows_managed_app_protections import WindowsManagedAppProtectionsRequest
		return WindowsManagedAppProtectionsRequest(self.request_adapter, self.path_parameters)

	@property
	def windows_management_app(self,
	) -> WindowsManagementAppRequest:
		from .windows_management_app import WindowsManagementAppRequest
		return WindowsManagementAppRequest(self.request_adapter, self.path_parameters)

