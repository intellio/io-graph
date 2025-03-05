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
	from .windows_information_protection_policies import WindowsInformationProtectionPoliciesRequest
	from .vpp_tokens import VppTokensRequest
	from .targeted_managed_app_configurations import TargetedManagedAppConfigurationsRequest
	from .mobile_apps import MobileAppsRequest
	from .mobile_app_configurations import MobileAppConfigurationsRequest
	from .mobile_app_categories import MobileAppCategoriesRequest
	from .sync_microsoft_store_for_business_apps import SyncMicrosoftStoreForBusinessAppsRequest
	from .mdm_windows_information_protection_policies import MdmWindowsInformationProtectionPoliciesRequest
	from .managed_e_books import ManagedEBooksRequest
	from .managed_app_statuses import ManagedAppStatusesRequest
	from .managed_app_registrations import ManagedAppRegistrationsRequest
	from .managed_app_policies import ManagedAppPoliciesRequest
	from .ios_managed_app_protections import IosManagedAppProtectionsRequest
	from .default_managed_app_protections import DefaultManagedAppProtectionsRequest
	from .android_managed_app_protections import AndroidManagedAppProtectionsRequest
	from ...request_adapter import HttpxRequestAdapter
from iograph_models.models.o_data_errors__o_data_error import ODataErrorsODataError
from iograph_models.models.device_app_management import DeviceAppManagement


class DeviceAppManagementRequest(BaseRequestBuilder):
	def __init__(self,request_adapter: HttpxRequestAdapter, path_parameters: Optional[Union[dict[str, Any], str]]) -> None:
		super().__init__(request_adapter, "{+baseurl}/deviceAppManagement", path_parameters)

	async def get(
		self,
		request_configuration: Optional[RequestConfiguration[GetQueryParams]] = None,
	) -> DeviceAppManagement:
		"""
		Get deviceAppManagement
		Read properties and relationships of the deviceAppManagement object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-onboarding-deviceappmanagement-get?view=graph-rest-1.0
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
		Update the properties of a deviceAppManagement object.
		Find more info here: https://learn.microsoft.com/graph/api/intune-books-deviceappmanagement-update?view=graph-rest-1.0
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
	def mobile_apps(self,
	) -> MobileAppsRequest:
		from .mobile_apps import MobileAppsRequest
		return MobileAppsRequest(self.request_adapter, self.path_parameters)

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
	def windows_information_protection_policies(self,
	) -> WindowsInformationProtectionPoliciesRequest:
		from .windows_information_protection_policies import WindowsInformationProtectionPoliciesRequest
		return WindowsInformationProtectionPoliciesRequest(self.request_adapter, self.path_parameters)

