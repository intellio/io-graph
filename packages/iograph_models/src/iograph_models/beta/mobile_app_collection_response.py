from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class MobileAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidForWorkApp, AndroidManagedStoreWebApp, AndroidStoreApp, IosiPadOSWebClip, IosStoreApp, IosVppApp, MacOSMicrosoftDefenderApp, MacOSMicrosoftEdgeApp, MacOSOfficeSuiteApp, MacOsVppApp, MacOSWebClip, ManagedAndroidStoreApp, ManagedIOSStoreApp, ManagedAndroidLobApp, ManagedIOSLobApp, MicrosoftStoreForBusinessApp, AndroidLobApp, IosLobApp, MacOSDmgApp, MacOSLobApp, MacOSPkgApp, Win32CatalogApp, WindowsAppX, WindowsMobileMSI, WindowsPhone81AppXBundle, WindowsPhoneXAP, WindowsUniversalAppX, OfficeSuiteApp, WebApp, WindowsMicrosoftEdgeApp, WindowsPhone81StoreApp, WindowsStoreApp, WindowsWebApp, WinGetApp],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

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
