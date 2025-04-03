from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceAppManagement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceAppManagement"] = Field(alias="@odata.type", default="#microsoft.graph.deviceAppManagement")
	isEnabledForMicrosoftStoreForBusiness: Optional[bool] = Field(alias="isEnabledForMicrosoftStoreForBusiness", default=None,)
	microsoftStoreForBusinessLanguage: Optional[str] = Field(alias="microsoftStoreForBusinessLanguage", default=None,)
	microsoftStoreForBusinessLastCompletedApplicationSyncTime: Optional[datetime] = Field(alias="microsoftStoreForBusinessLastCompletedApplicationSyncTime", default=None,)
	microsoftStoreForBusinessLastSuccessfulSyncDateTime: Optional[datetime] = Field(alias="microsoftStoreForBusinessLastSuccessfulSyncDateTime", default=None,)
	microsoftStoreForBusinessPortalSelection: Optional[MicrosoftStoreForBusinessPortalSelectionOptions | str] = Field(alias="microsoftStoreForBusinessPortalSelection", default=None,)
	androidManagedAppProtections: Optional[list[AndroidManagedAppProtection]] = Field(alias="androidManagedAppProtections", default=None,)
	defaultManagedAppProtections: Optional[list[DefaultManagedAppProtection]] = Field(alias="defaultManagedAppProtections", default=None,)
	deviceAppManagementTasks: Optional[list[Annotated[Union[AppVulnerabilityTask, SecurityConfigurationTask, UnmanagedDeviceDiscoveryTask],Field(discriminator="odata_type")]]] = Field(alias="deviceAppManagementTasks", default=None,)
	enterpriseCodeSigningCertificates: Optional[list[EnterpriseCodeSigningCertificate]] = Field(alias="enterpriseCodeSigningCertificates", default=None,)
	iosLobAppProvisioningConfigurations: Optional[list[IosLobAppProvisioningConfiguration]] = Field(alias="iosLobAppProvisioningConfigurations", default=None,)
	iosManagedAppProtections: Optional[list[IosManagedAppProtection]] = Field(alias="iosManagedAppProtections", default=None,)
	managedAppPolicies: Optional[list[Annotated[Union[TargetedManagedAppConfiguration, DefaultManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy, WindowsManagedAppProtection],Field(discriminator="odata_type")]]] = Field(alias="managedAppPolicies", default=None,)
	managedAppRegistrations: Optional[list[Annotated[Union[AndroidManagedAppRegistration, IosManagedAppRegistration, WindowsManagedAppRegistration],Field(discriminator="odata_type")]]] = Field(alias="managedAppRegistrations", default=None,)
	managedAppStatuses: Optional[list[Annotated[Union[ManagedAppStatusRaw],Field(discriminator="odata_type")]]] = Field(alias="managedAppStatuses", default=None,)
	managedEBookCategories: Optional[list[ManagedEBookCategory]] = Field(alias="managedEBookCategories", default=None,)
	managedEBooks: Optional[list[Annotated[Union[IosVppEBook],Field(discriminator="odata_type")]]] = Field(alias="managedEBooks", default=None,)
	mdmWindowsInformationProtectionPolicies: Optional[list[MdmWindowsInformationProtectionPolicy]] = Field(alias="mdmWindowsInformationProtectionPolicies", default=None,)
	mobileAppCatalogPackages: Optional[list[Annotated[Union[Win32MobileAppCatalogPackage],Field(discriminator="odata_type")]]] = Field(alias="mobileAppCatalogPackages", default=None,)
	mobileAppCategories: Optional[list[MobileAppCategory]] = Field(alias="mobileAppCategories", default=None,)
	mobileAppConfigurations: Optional[list[Annotated[Union[AndroidForWorkMobileAppConfiguration, AndroidManagedStoreAppConfiguration, IosMobileAppConfiguration],Field(discriminator="odata_type")]]] = Field(alias="mobileAppConfigurations", default=None,)
	mobileAppRelationships: Optional[list[Annotated[Union[MobileAppDependency, MobileAppSupersedence],Field(discriminator="odata_type")]]] = Field(alias="mobileAppRelationships", default=None,)
	mobileApps: Optional[list[Annotated[Union[AndroidForWorkApp, AndroidManagedStoreWebApp, AndroidStoreApp, IosiPadOSWebClip, IosStoreApp, IosVppApp, MacOSMicrosoftDefenderApp, MacOSMicrosoftEdgeApp, MacOSOfficeSuiteApp, MacOsVppApp, MacOSWebClip, ManagedAndroidStoreApp, ManagedIOSStoreApp, ManagedAndroidLobApp, ManagedIOSLobApp, MicrosoftStoreForBusinessApp, AndroidLobApp, IosLobApp, MacOSDmgApp, MacOSLobApp, MacOSPkgApp, Win32CatalogApp, WindowsAppX, WindowsMobileMSI, WindowsPhone81AppXBundle, WindowsPhoneXAP, WindowsUniversalAppX, OfficeSuiteApp, WebApp, WindowsMicrosoftEdgeApp, WindowsPhone81StoreApp, WindowsStoreApp, WindowsWebApp, WinGetApp],Field(discriminator="odata_type")]]] = Field(alias="mobileApps", default=None,)
	policySets: Optional[list[PolicySet]] = Field(alias="policySets", default=None,)
	symantecCodeSigningCertificate: Optional[SymantecCodeSigningCertificate] = Field(alias="symantecCodeSigningCertificate", default=None,)
	targetedManagedAppConfigurations: Optional[list[TargetedManagedAppConfiguration]] = Field(alias="targetedManagedAppConfigurations", default=None,)
	vppTokens: Optional[list[VppToken]] = Field(alias="vppTokens", default=None,)
	wdacSupplementalPolicies: Optional[list[WindowsDefenderApplicationControlSupplementalPolicy]] = Field(alias="wdacSupplementalPolicies", default=None,)
	windowsInformationProtectionDeviceRegistrations: Optional[list[WindowsInformationProtectionDeviceRegistration]] = Field(alias="windowsInformationProtectionDeviceRegistrations", default=None,)
	windowsInformationProtectionPolicies: Optional[list[WindowsInformationProtectionPolicy]] = Field(alias="windowsInformationProtectionPolicies", default=None,)
	windowsInformationProtectionWipeActions: Optional[list[WindowsInformationProtectionWipeAction]] = Field(alias="windowsInformationProtectionWipeActions", default=None,)
	windowsManagedAppProtections: Optional[list[WindowsManagedAppProtection]] = Field(alias="windowsManagedAppProtections", default=None,)
	windowsManagementApp: Optional[WindowsManagementApp] = Field(alias="windowsManagementApp", default=None,)

from .microsoft_store_for_business_portal_selection_options import MicrosoftStoreForBusinessPortalSelectionOptions
from .android_managed_app_protection import AndroidManagedAppProtection
from .default_managed_app_protection import DefaultManagedAppProtection
from .app_vulnerability_task import AppVulnerabilityTask
from .security_configuration_task import SecurityConfigurationTask
from .unmanaged_device_discovery_task import UnmanagedDeviceDiscoveryTask
from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
from .ios_managed_app_protection import IosManagedAppProtection
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .windows_information_protection_policy import WindowsInformationProtectionPolicy
from .windows_managed_app_protection import WindowsManagedAppProtection
from .android_managed_app_registration import AndroidManagedAppRegistration
from .ios_managed_app_registration import IosManagedAppRegistration
from .windows_managed_app_registration import WindowsManagedAppRegistration
from .managed_app_status_raw import ManagedAppStatusRaw
from .managed_e_book_category import ManagedEBookCategory
from .ios_vpp_e_book import IosVppEBook
from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage
from .mobile_app_category import MobileAppCategory
from .android_for_work_mobile_app_configuration import AndroidForWorkMobileAppConfiguration
from .android_managed_store_app_configuration import AndroidManagedStoreAppConfiguration
from .ios_mobile_app_configuration import IosMobileAppConfiguration
from .mobile_app_dependency import MobileAppDependency
from .mobile_app_supersedence import MobileAppSupersedence
from .android_for_work_app import AndroidForWorkApp
from .android_managed_store_web_app import AndroidManagedStoreWebApp
from .android_store_app import AndroidStoreApp
from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
from .ios_store_app import IosStoreApp
from .ios_vpp_app import IosVppApp
from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
from .mac_os_vpp_app import MacOsVppApp
from .mac_o_s_web_clip import MacOSWebClip
from .managed_android_store_app import ManagedAndroidStoreApp
from .managed_i_o_s_store_app import ManagedIOSStoreApp
from .managed_android_lob_app import ManagedAndroidLobApp
from .managed_i_o_s_lob_app import ManagedIOSLobApp
from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
from .android_lob_app import AndroidLobApp
from .ios_lob_app import IosLobApp
from .mac_o_s_dmg_app import MacOSDmgApp
from .mac_o_s_lob_app import MacOSLobApp
from .mac_o_s_pkg_app import MacOSPkgApp
from .win32_catalog_app import Win32CatalogApp
from .windows_app_x import WindowsAppX
from .windows_mobile_m_s_i import WindowsMobileMSI
from .windows_phone81_app_x_bundle import WindowsPhone81AppXBundle
from .windows_phone_x_a_p import WindowsPhoneXAP
from .windows_universal_app_x import WindowsUniversalAppX
from .office_suite_app import OfficeSuiteApp
from .web_app import WebApp
from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
from .windows_phone81_store_app import WindowsPhone81StoreApp
from .windows_store_app import WindowsStoreApp
from .windows_web_app import WindowsWebApp
from .win_get_app import WinGetApp
from .policy_set import PolicySet
from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
from .vpp_token import VppToken
from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
from .windows_management_app import WindowsManagementApp
