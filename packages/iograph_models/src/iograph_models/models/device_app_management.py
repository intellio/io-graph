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
	androidManagedAppProtections: Optional[list[AndroidManagedAppProtection]] = Field(alias="androidManagedAppProtections",default=None,)
	defaultManagedAppProtections: Optional[list[DefaultManagedAppProtection]] = Field(alias="defaultManagedAppProtections",default=None,)
	iosManagedAppProtections: Optional[list[IosManagedAppProtection]] = Field(alias="iosManagedAppProtections",default=None,)
	managedAppPolicies: SerializeAsAny[Optional[list[ManagedAppPolicy]]] = Field(alias="managedAppPolicies",default=None,)
	managedAppRegistrations: SerializeAsAny[Optional[list[ManagedAppRegistration]]] = Field(alias="managedAppRegistrations",default=None,)
	managedAppStatuses: SerializeAsAny[Optional[list[ManagedAppStatus]]] = Field(alias="managedAppStatuses",default=None,)
	managedEBooks: SerializeAsAny[Optional[list[ManagedEBook]]] = Field(alias="managedEBooks",default=None,)
	mdmWindowsInformationProtectionPolicies: Optional[list[MdmWindowsInformationProtectionPolicy]] = Field(alias="mdmWindowsInformationProtectionPolicies",default=None,)
	mobileAppCategories: Optional[list[MobileAppCategory]] = Field(alias="mobileAppCategories",default=None,)
	mobileAppConfigurations: SerializeAsAny[Optional[list[ManagedDeviceMobileAppConfiguration]]] = Field(alias="mobileAppConfigurations",default=None,)
	mobileApps: SerializeAsAny[Optional[list[MobileApp]]] = Field(alias="mobileApps",default=None,)
	targetedManagedAppConfigurations: Optional[list[TargetedManagedAppConfiguration]] = Field(alias="targetedManagedAppConfigurations",default=None,)
	vppTokens: Optional[list[VppToken]] = Field(alias="vppTokens",default=None,)
	windowsInformationProtectionPolicies: Optional[list[WindowsInformationProtectionPolicy]] = Field(alias="windowsInformationProtectionPolicies",default=None,)

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

