from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsKioskSingleWin32App(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsKioskSingleWin32App"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskSingleWin32App")
	win32App: Optional[WindowsKioskWin32App] = Field(alias="win32App", default=None,)

from .windows_kiosk_win32_app import WindowsKioskWin32App
