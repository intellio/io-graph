from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppInstallStatus(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	displayVersion: Optional[str] = Field(alias="displayVersion", default=None,)
	errorCode: Optional[int] = Field(alias="errorCode", default=None,)
	installState: Optional[ResultantAppState | str] = Field(alias="installState", default=None,)
	installStateDetail: Optional[ResultantAppStateDetail | str] = Field(alias="installStateDetail", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	mobileAppInstallStatusValue: Optional[ResultantAppState | str] = Field(alias="mobileAppInstallStatusValue", default=None,)
	osDescription: Optional[str] = Field(alias="osDescription", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	app: Optional[Union[AndroidForWorkApp, AndroidManagedStoreApp, AndroidManagedStoreWebApp, AndroidStoreApp, IosiPadOSWebClip, IosStoreApp, IosVppApp, MacOSMicrosoftDefenderApp, MacOSMicrosoftEdgeApp, MacOSOfficeSuiteApp, MacOsVppApp, MacOSWebClip, ManagedApp, ManagedAndroidStoreApp, ManagedIOSStoreApp, ManagedMobileLobApp, ManagedAndroidLobApp, ManagedIOSLobApp, MicrosoftStoreForBusinessApp, MobileLobApp, AndroidLobApp, IosLobApp, MacOSDmgApp, MacOSLobApp, MacOSPkgApp, Win32LobApp, Win32CatalogApp, WindowsAppX, WindowsMobileMSI, WindowsPhone81AppX, WindowsPhone81AppXBundle, WindowsPhoneXAP, WindowsUniversalAppX, OfficeSuiteApp, WebApp, WindowsMicrosoftEdgeApp, WindowsPhone81StoreApp, WindowsStoreApp, WindowsWebApp, WinGetApp]] = Field(alias="app", default=None,discriminator="odata_type", )

from .resultant_app_state import ResultantAppState
from .resultant_app_state_detail import ResultantAppStateDetail
from .resultant_app_state import ResultantAppState
from .android_for_work_app import AndroidForWorkApp
from .android_managed_store_app import AndroidManagedStoreApp
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
from .mac_o_s_pkg_app import MacOSPkgApp
from .win32_lob_app import Win32LobApp
from .win32_catalog_app import Win32CatalogApp
from .windows_app_x import WindowsAppX
from .windows_mobile_m_s_i import WindowsMobileMSI
from .windows_phone81_app_x import WindowsPhone81AppX
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

