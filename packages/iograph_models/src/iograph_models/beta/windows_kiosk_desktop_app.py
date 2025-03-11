from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskDesktopApp(BaseModel):
	appType: Optional[WindowsKioskAppType | str] = Field(alias="appType",default=None,)
	autoLaunch: Optional[bool] = Field(alias="autoLaunch",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	startLayoutTileSize: Optional[WindowsAppStartLayoutTileSize | str] = Field(alias="startLayoutTileSize",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	desktopApplicationId: Optional[str] = Field(alias="desktopApplicationId",default=None,)
	desktopApplicationLinkPath: Optional[str] = Field(alias="desktopApplicationLinkPath",default=None,)
	path: Optional[str] = Field(alias="path",default=None,)

from .windows_kiosk_app_type import WindowsKioskAppType
from .windows_app_start_layout_tile_size import WindowsAppStartLayoutTileSize

