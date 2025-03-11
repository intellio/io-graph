from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskSingleWin32App(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	win32App: Optional[WindowsKioskWin32App] = Field(alias="win32App",default=None,)

from .windows_kiosk_win32_app import WindowsKioskWin32App

