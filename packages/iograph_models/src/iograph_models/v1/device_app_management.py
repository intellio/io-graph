from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAppManagement(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	isEnabledForMicrosoftStoreForBusiness: Optional[bool] = Field(alias="isEnabledForMicrosoftStoreForBusiness", default=None,)
	microsoftStoreForBusinessLanguage: Optional[str] = Field(alias="microsoftStoreForBusinessLanguage", default=None,)
	microsoftStoreForBusinessLastCompletedApplicationSyncTime: Optional[datetime] = Field(alias="microsoftStoreForBusinessLastCompletedApplicationSyncTime", default=None,)
	microsoftStoreForBusinessLastSuccessfulSyncDateTime: Optional[datetime] = Field(alias="microsoftStoreForBusinessLastSuccessfulSyncDateTime", default=None,)
	androidManagedAppProtections: Optional[list[AndroidManagedAppProtection]] = Field(alias="androidManagedAppProtections", default=None,)
	defaultManagedAppProtections: Optional[list[DefaultManagedAppProtection]] = Field(alias="defaultManagedAppProtections", default=None,)
	iosManagedAppProtections: Optional[list[IosManagedAppProtection]] = Field(alias="iosManagedAppProtections", default=None,)
	managedAppPolicies: Optional[list[Annotated[Union[ManagedAppConfiguration, TargetedManagedAppConfiguration, ManagedAppProtection, DefaultManagedAppProtection, TargetedManagedAppProtection, AndroidManagedAppProtection, IosManagedAppProtection, WindowsInformationProtection, MdmWindowsInformationProtectionPolicy, WindowsInformationProtectionPolicy],Field(discriminator="odata_type")]]] = Field(alias="managedAppPolicies", default=None,)
	managedAppRegistrations: Optional[list[Annotated[Union[AndroidManagedAppRegistration, IosManagedAppRegistration],Field(discriminator="odata_type")]]] = Field(alias="managedAppRegistrations", default=None,)
	managedAppStatuses: Optional[list[Annotated[Union[ManagedAppStatusRaw],Field(discriminator="odata_type")]]] = Field(alias="managedAppStatuses", default=None,)
	managedEBooks: Optional[list[Annotated[Union[IosVppEBook],Field(discriminator="odata_type")]]] = Field(alias="managedEBooks", default=None,)
	mdmWindowsInformationProtectionPolicies: Optional[list[MdmWindowsInformationProtectionPolicy]] = Field(alias="mdmWindowsInformationProtectionPolicies", default=None,)
	mobileAppCategories: Optional[list[MobileAppCategory]] = Field(alias="mobileAppCategories", default=None,)
	mobileAppConfigurations: Optional[list[Annotated[Union[IosMobileAppConfiguration],Field(discriminator="odata_type")]]] = Field(alias="mobileAppConfigurations", default=None,)
	mobileApps: Optional[list[Annotated[Union[AndroidStoreApp, IosiPadOSWebClip, IosStoreApp, IosVppApp, MacOSMicrosoftDefenderApp, MacOSMicrosoftEdgeApp, MacOSOfficeSuiteApp, ManagedApp, ManagedAndroidStoreApp, ManagedIOSStoreApp, ManagedMobileLobApp, ManagedAndroidLobApp, ManagedIOSLobApp, MicrosoftStoreForBusinessApp, MobileLobApp, AndroidLobApp, IosLobApp, MacOSDmgApp, MacOSLobApp, Win32LobApp, WindowsAppX, WindowsMobileMSI, WindowsUniversalAppX, WebApp, WindowsMicrosoftEdgeApp, WindowsWebApp],Field(discriminator="odata_type")]]] = Field(alias="mobileApps", default=None,)
	targetedManagedAppConfigurations: Optional[list[TargetedManagedAppConfiguration]] = Field(alias="targetedManagedAppConfigurations", default=None,)
	vppTokens: Optional[list[VppToken]] = Field(alias="vppTokens", default=None,)
	windowsInformationProtectionPolicies: Optional[list[WindowsInformationProtectionPolicy]] = Field(alias="windowsInformationProtectionPolicies", default=None,)

from .android_managed_app_protection import AndroidManagedAppProtection
from .default_managed_app_protection import DefaultManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection
from .managed_app_configuration import ManagedAppConfiguration
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .managed_app_protection import ManagedAppProtection
from .default_managed_app_protection import DefaultManagedAppProtection
from .targeted_managed_app_protection import TargetedManagedAppProtection
from .android_managed_app_protection import AndroidManagedAppProtection
from .ios_managed_app_protection import IosManagedAppProtection
from .windows_information_protection import WindowsInformationProtection
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .windows_information_protection_policy import WindowsInformationProtectionPolicy
from .android_managed_app_registration import AndroidManagedAppRegistration
from .ios_managed_app_registration import IosManagedAppRegistration
from .managed_app_status_raw import ManagedAppStatusRaw
from .ios_vpp_e_book import IosVppEBook
from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
from .mobile_app_category import MobileAppCategory
from .ios_mobile_app_configuration import IosMobileAppConfiguration
from .android_store_app import AndroidStoreApp
from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
from .ios_store_app import IosStoreApp
from .ios_vpp_app import IosVppApp
from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
from .managed_app import ManagedApp
from .managed_android_store_app import ManagedAndroidStoreApp
from .managed_i_o_s_store_app import ManagedIOSStoreApp
from .managed_mobile_lob_app import ManagedMobileLobApp
from .managed_android_lob_app import ManagedAndroidLobApp
from .managed_i_o_s_lob_app import ManagedIOSLobApp
from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
from .mobile_lob_app import MobileLobApp
from .android_lob_app import AndroidLobApp
from .ios_lob_app import IosLobApp
from .mac_o_s_dmg_app import MacOSDmgApp
from .mac_o_s_lob_app import MacOSLobApp
from .win32_lob_app import Win32LobApp
from .windows_app_x import WindowsAppX
from .windows_mobile_m_s_i import WindowsMobileMSI
from .windows_universal_app_x import WindowsUniversalAppX
from .web_app import WebApp
from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
from .windows_web_app import WindowsWebApp
from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
from .vpp_token import VppToken
from .windows_information_protection_policy import WindowsInformationProtectionPolicy

