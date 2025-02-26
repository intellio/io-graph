from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceAppManagement(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isEnabledForMicrosoftStoreForBusiness: Optional[bool] = Field(default=None,alias="isEnabledForMicrosoftStoreForBusiness",)
	microsoftStoreForBusinessLanguage: Optional[str] = Field(default=None,alias="microsoftStoreForBusinessLanguage",)
	microsoftStoreForBusinessLastCompletedApplicationSyncTime: Optional[datetime] = Field(default=None,alias="microsoftStoreForBusinessLastCompletedApplicationSyncTime",)
	microsoftStoreForBusinessLastSuccessfulSyncDateTime: Optional[datetime] = Field(default=None,alias="microsoftStoreForBusinessLastSuccessfulSyncDateTime",)
	androidManagedAppProtections: list[AndroidManagedAppProtection] = Field(alias="androidManagedAppProtections",)
	defaultManagedAppProtections: list[DefaultManagedAppProtection] = Field(alias="defaultManagedAppProtections",)
	iosManagedAppProtections: list[IosManagedAppProtection] = Field(alias="iosManagedAppProtections",)
	managedAppPolicies: list[ManagedAppPolicy] = Field(alias="managedAppPolicies",)
	managedAppRegistrations: list[ManagedAppRegistration] = Field(alias="managedAppRegistrations",)
	managedAppStatuses: list[ManagedAppStatus] = Field(alias="managedAppStatuses",)
	managedEBooks: list[ManagedEBook] = Field(alias="managedEBooks",)
	mdmWindowsInformationProtectionPolicies: list[MdmWindowsInformationProtectionPolicy] = Field(alias="mdmWindowsInformationProtectionPolicies",)
	mobileAppCategories: list[MobileAppCategory] = Field(alias="mobileAppCategories",)
	mobileAppConfigurations: list[ManagedDeviceMobileAppConfiguration] = Field(alias="mobileAppConfigurations",)
	mobileApps: list[MobileApp] = Field(alias="mobileApps",)
	targetedManagedAppConfigurations: list[TargetedManagedAppConfiguration] = Field(alias="targetedManagedAppConfigurations",)
	vppTokens: list[VppToken] = Field(alias="vppTokens",)
	windowsInformationProtectionPolicies: list[WindowsInformationProtectionPolicy] = Field(alias="windowsInformationProtectionPolicies",)

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

