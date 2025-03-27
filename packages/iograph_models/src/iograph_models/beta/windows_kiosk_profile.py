from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskProfile(BaseModel):
	appConfiguration: Optional[Union[WindowsKioskMultipleApps, WindowsKioskSingleUWPApp, WindowsKioskSingleWin32App]] = Field(alias="appConfiguration", default=None,discriminator="odata_type", )
	profileId: Optional[str] = Field(alias="profileId", default=None,)
	profileName: Optional[str] = Field(alias="profileName", default=None,)
	userAccountsConfiguration: Optional[list[Annotated[Union[WindowsKioskActiveDirectoryGroup, WindowsKioskAutologon, WindowsKioskAzureADGroup, WindowsKioskAzureADUser, WindowsKioskLocalGroup, WindowsKioskLocalUser, WindowsKioskVisitor]],Field(discriminator="odata_type")]]] = Field(alias="userAccountsConfiguration", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_kiosk_multiple_apps import WindowsKioskMultipleApps
from .windows_kiosk_single_u_w_p_app import WindowsKioskSingleUWPApp
from .windows_kiosk_single_win32_app import WindowsKioskSingleWin32App
from .windows_kiosk_active_directory_group import WindowsKioskActiveDirectoryGroup
from .windows_kiosk_autologon import WindowsKioskAutologon
from .windows_kiosk_azure_a_d_group import WindowsKioskAzureADGroup
from .windows_kiosk_azure_a_d_user import WindowsKioskAzureADUser
from .windows_kiosk_local_group import WindowsKioskLocalGroup
from .windows_kiosk_local_user import WindowsKioskLocalUser
from .windows_kiosk_visitor import WindowsKioskVisitor

