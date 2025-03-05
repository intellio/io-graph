from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAppManagement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isEnabledForMicrosoftStoreForBusiness: Optional[bool] = Field(default=None,alias="isEnabledForMicrosoftStoreForBusiness",)
	microsoftStoreForBusinessLanguage: Optional[str] = Field(default=None,alias="microsoftStoreForBusinessLanguage",)
	microsoftStoreForBusinessLastCompletedApplicationSyncTime: Optional[datetime] = Field(default=None,alias="microsoftStoreForBusinessLastCompletedApplicationSyncTime",)
	microsoftStoreForBusinessLastSuccessfulSyncDateTime: Optional[datetime] = Field(default=None,alias="microsoftStoreForBusinessLastSuccessfulSyncDateTime",)
	androidManagedAppProtections: Optional[list[AndroidManagedAppProtection]] = Field(default=None,alias="androidManagedAppProtections",)
	defaultManagedAppProtections: Optional[list[DefaultManagedAppProtection]] = Field(default=None,alias="defaultManagedAppProtections",)
	iosManagedAppProtections: Optional[list[IosManagedAppProtection]] = Field(default=None,alias="iosManagedAppProtections",)
	managedAppPolicies: Optional[list[ManagedAppPolicy]] = Field(default=None,alias="managedAppPolicies",)
	managedAppRegistrations: Optional[list[ManagedAppRegistration]] = Field(default=None,alias="managedAppRegistrations",)
	managedAppStatuses: Optional[list[ManagedAppStatus]] = Field(default=None,alias="managedAppStatuses",)
	managedEBooks: Optional[list[ManagedEBook]] = Field(default=None,alias="managedEBooks",)
	mdmWindowsInformationProtectionPolicies: Optional[list[MdmWindowsInformationProtectionPolicy]] = Field(default=None,alias="mdmWindowsInformationProtectionPolicies",)
	mobileAppCategories: Optional[list[MobileAppCategory]] = Field(default=None,alias="mobileAppCategories",)
	mobileAppConfigurations: Optional[list[ManagedDeviceMobileAppConfiguration]] = Field(default=None,alias="mobileAppConfigurations",)
	mobileApps: Optional[list[MobileApp]] = Field(default=None,alias="mobileApps",)
	targetedManagedAppConfigurations: Optional[list[TargetedManagedAppConfiguration]] = Field(default=None,alias="targetedManagedAppConfigurations",)
	vppTokens: Optional[list[VppToken]] = Field(default=None,alias="vppTokens",)
	windowsInformationProtectionPolicies: Optional[list[WindowsInformationProtectionPolicy]] = Field(default=None,alias="windowsInformationProtectionPolicies",)

from .android_managed_app_protection import AndroidManagedAppProtection
from .default_managed_app_protection import DefaultManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection
from .managed_app_policy import ManagedAppPolicy
from .managed_app_registration import ManagedAppRegistration
from .managed_app_status import ManagedAppStatus
from .managed_e_book import ManagedEBook
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .mobile_app_category import MobileAppCategory
from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
from .mobile_app import MobileApp
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .vpp_token import VppToken
from .windows_information_protection_policy import WindowsInformationProtectionPolicy

