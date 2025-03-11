from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAppManagement(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	isEnabledForMicrosoftStoreForBusiness: Optional[bool] = Field(alias="isEnabledForMicrosoftStoreForBusiness",default=None,)
	microsoftStoreForBusinessLanguage: Optional[str] = Field(alias="microsoftStoreForBusinessLanguage",default=None,)
	microsoftStoreForBusinessLastCompletedApplicationSyncTime: Optional[datetime] = Field(alias="microsoftStoreForBusinessLastCompletedApplicationSyncTime",default=None,)
	microsoftStoreForBusinessLastSuccessfulSyncDateTime: Optional[datetime] = Field(alias="microsoftStoreForBusinessLastSuccessfulSyncDateTime",default=None,)
	microsoftStoreForBusinessPortalSelection: Optional[MicrosoftStoreForBusinessPortalSelectionOptions | str] = Field(alias="microsoftStoreForBusinessPortalSelection",default=None,)
	androidManagedAppProtections: Optional[list[AndroidManagedAppProtection]] = Field(alias="androidManagedAppProtections",default=None,)
	defaultManagedAppProtections: Optional[list[DefaultManagedAppProtection]] = Field(alias="defaultManagedAppProtections",default=None,)
	deviceAppManagementTasks: SerializeAsAny[Optional[list[DeviceAppManagementTask]]] = Field(alias="deviceAppManagementTasks",default=None,)
	enterpriseCodeSigningCertificates: Optional[list[EnterpriseCodeSigningCertificate]] = Field(alias="enterpriseCodeSigningCertificates",default=None,)
	iosLobAppProvisioningConfigurations: Optional[list[IosLobAppProvisioningConfiguration]] = Field(alias="iosLobAppProvisioningConfigurations",default=None,)
	iosManagedAppProtections: Optional[list[IosManagedAppProtection]] = Field(alias="iosManagedAppProtections",default=None,)
	managedAppPolicies: SerializeAsAny[Optional[list[ManagedAppPolicy]]] = Field(alias="managedAppPolicies",default=None,)
	managedAppRegistrations: SerializeAsAny[Optional[list[ManagedAppRegistration]]] = Field(alias="managedAppRegistrations",default=None,)
	managedAppStatuses: SerializeAsAny[Optional[list[ManagedAppStatus]]] = Field(alias="managedAppStatuses",default=None,)
	managedEBookCategories: Optional[list[ManagedEBookCategory]] = Field(alias="managedEBookCategories",default=None,)
	managedEBooks: SerializeAsAny[Optional[list[ManagedEBook]]] = Field(alias="managedEBooks",default=None,)
	mdmWindowsInformationProtectionPolicies: Optional[list[MdmWindowsInformationProtectionPolicy]] = Field(alias="mdmWindowsInformationProtectionPolicies",default=None,)
	mobileAppCatalogPackages: SerializeAsAny[Optional[list[MobileAppCatalogPackage]]] = Field(alias="mobileAppCatalogPackages",default=None,)
	mobileAppCategories: Optional[list[MobileAppCategory]] = Field(alias="mobileAppCategories",default=None,)
	mobileAppConfigurations: SerializeAsAny[Optional[list[ManagedDeviceMobileAppConfiguration]]] = Field(alias="mobileAppConfigurations",default=None,)
	mobileAppRelationships: SerializeAsAny[Optional[list[MobileAppRelationship]]] = Field(alias="mobileAppRelationships",default=None,)
	mobileApps: SerializeAsAny[Optional[list[MobileApp]]] = Field(alias="mobileApps",default=None,)
	policySets: Optional[list[PolicySet]] = Field(alias="policySets",default=None,)
	symantecCodeSigningCertificate: Optional[SymantecCodeSigningCertificate] = Field(alias="symantecCodeSigningCertificate",default=None,)
	targetedManagedAppConfigurations: Optional[list[TargetedManagedAppConfiguration]] = Field(alias="targetedManagedAppConfigurations",default=None,)
	vppTokens: Optional[list[VppToken]] = Field(alias="vppTokens",default=None,)
	wdacSupplementalPolicies: Optional[list[WindowsDefenderApplicationControlSupplementalPolicy]] = Field(alias="wdacSupplementalPolicies",default=None,)
	windowsInformationProtectionDeviceRegistrations: Optional[list[WindowsInformationProtectionDeviceRegistration]] = Field(alias="windowsInformationProtectionDeviceRegistrations",default=None,)
	windowsInformationProtectionPolicies: Optional[list[WindowsInformationProtectionPolicy]] = Field(alias="windowsInformationProtectionPolicies",default=None,)
	windowsInformationProtectionWipeActions: Optional[list[WindowsInformationProtectionWipeAction]] = Field(alias="windowsInformationProtectionWipeActions",default=None,)
	windowsManagedAppProtections: Optional[list[WindowsManagedAppProtection]] = Field(alias="windowsManagedAppProtections",default=None,)
	windowsManagementApp: Optional[WindowsManagementApp] = Field(alias="windowsManagementApp",default=None,)

from .microsoft_store_for_business_portal_selection_options import MicrosoftStoreForBusinessPortalSelectionOptions
from .android_managed_app_protection import AndroidManagedAppProtection
from .default_managed_app_protection import DefaultManagedAppProtection
from .device_app_management_task import DeviceAppManagementTask
from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
from .ios_lob_app_provisioning_configuration import IosLobAppProvisioningConfiguration
from .ios_managed_app_protection import IosManagedAppProtection
from .managed_app_policy import ManagedAppPolicy
from .managed_app_registration import ManagedAppRegistration
from .managed_app_status import ManagedAppStatus
from .managed_e_book_category import ManagedEBookCategory
from .managed_e_book import ManagedEBook
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .mobile_app_catalog_package import MobileAppCatalogPackage
from .mobile_app_category import MobileAppCategory
from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
from .mobile_app_relationship import MobileAppRelationship
from .mobile_app import MobileApp
from .policy_set import PolicySet
from .symantec_code_signing_certificate import SymantecCodeSigningCertificate
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .vpp_token import VppToken
from .windows_defender_application_control_supplemental_policy import WindowsDefenderApplicationControlSupplementalPolicy
from .windows_information_protection_device_registration import WindowsInformationProtectionDeviceRegistration
from .windows_information_protection_policy import WindowsInformationProtectionPolicy
from .windows_information_protection_wipe_action import WindowsInformationProtectionWipeAction
from .windows_managed_app_protection import WindowsManagedAppProtection
from .windows_management_app import WindowsManagementApp

