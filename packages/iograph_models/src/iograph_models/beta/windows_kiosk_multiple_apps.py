from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class WindowsKioskMultipleApps(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskMultipleApps"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskMultipleApps")
	allowAccessToDownloadsFolder: Optional[bool] = Field(alias="allowAccessToDownloadsFolder", default=None,)
	apps: Optional[list[Annotated[Union[WindowsKioskDesktopApp, WindowsKioskUWPApp, WindowsKioskWin32App],Field(discriminator="odata_type")]]] = Field(alias="apps", default=None,)
	disallowDesktopApps: Optional[bool] = Field(alias="disallowDesktopApps", default=None,)
	showTaskBar: Optional[bool] = Field(alias="showTaskBar", default=None,)
	startMenuLayoutXml: Optional[str] = Field(alias="startMenuLayoutXml", default=None,)

from .windows_kiosk_desktop_app import WindowsKioskDesktopApp
from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp
from .windows_kiosk_win32_app import WindowsKioskWin32App
