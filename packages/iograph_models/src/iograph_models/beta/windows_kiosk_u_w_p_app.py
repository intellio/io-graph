from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskUWPApp(BaseModel):
	appType: Optional[WindowsKioskAppType | str] = Field(alias="appType", default=None,)
	autoLaunch: Optional[bool] = Field(alias="autoLaunch", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	startLayoutTileSize: Optional[WindowsAppStartLayoutTileSize | str] = Field(alias="startLayoutTileSize", default=None,)
	odata_type: Literal["#microsoft.graph.windowsKioskUWPApp"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskUWPApp")
	appId: Optional[str] = Field(alias="appId", default=None,)
	appUserModelId: Optional[str] = Field(alias="appUserModelId", default=None,)
	containedAppId: Optional[str] = Field(alias="containedAppId", default=None,)

from .windows_kiosk_app_type import WindowsKioskAppType
from .windows_app_start_layout_tile_size import WindowsAppStartLayoutTileSize

