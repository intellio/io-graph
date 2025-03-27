from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MobileLobAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AndroidLobApp, IosLobApp, MacOSDmgApp, MacOSLobApp, MacOSPkgApp, Win32LobApp, Win32CatalogApp, WindowsAppX, WindowsMobileMSI, WindowsPhone81AppX, WindowsPhone81AppXBundle, WindowsPhoneXAP, WindowsUniversalAppX],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

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

