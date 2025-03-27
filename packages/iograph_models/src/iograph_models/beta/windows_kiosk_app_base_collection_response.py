from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskAppBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[WindowsKioskDesktopApp, WindowsKioskUWPApp, WindowsKioskWin32App]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows_kiosk_desktop_app import WindowsKioskDesktopApp
from .windows_kiosk_u_w_p_app import WindowsKioskUWPApp
from .windows_kiosk_win32_app import WindowsKioskWin32App

