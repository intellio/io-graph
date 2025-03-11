from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskMultipleApps(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowAccessToDownloadsFolder: Optional[bool] = Field(alias="allowAccessToDownloadsFolder",default=None,)
	apps: SerializeAsAny[Optional[list[WindowsKioskAppBase]]] = Field(alias="apps",default=None,)
	disallowDesktopApps: Optional[bool] = Field(alias="disallowDesktopApps",default=None,)
	showTaskBar: Optional[bool] = Field(alias="showTaskBar",default=None,)
	startMenuLayoutXml: Optional[str] = Field(alias="startMenuLayoutXml",default=None,)

from .windows_kiosk_app_base import WindowsKioskAppBase

