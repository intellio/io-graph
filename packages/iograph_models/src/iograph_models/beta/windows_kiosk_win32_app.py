from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsKioskWin32App(BaseModel):
	appType: Optional[WindowsKioskAppType | str] = Field(alias="appType", default=None,)
	autoLaunch: Optional[bool] = Field(alias="autoLaunch", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	startLayoutTileSize: Optional[WindowsAppStartLayoutTileSize | str] = Field(alias="startLayoutTileSize", default=None,)
	odata_type: Literal["#microsoft.graph.windowsKioskWin32App"] = Field(alias="@odata.type", default="#microsoft.graph.windowsKioskWin32App")
	classicAppPath: Optional[str] = Field(alias="classicAppPath", default=None,)
	edgeKiosk: Optional[str] = Field(alias="edgeKiosk", default=None,)
	edgeKioskIdleTimeoutMinutes: Optional[int] = Field(alias="edgeKioskIdleTimeoutMinutes", default=None,)
	edgeKioskType: Optional[WindowsEdgeKioskType | str] = Field(alias="edgeKioskType", default=None,)
	edgeNoFirstRun: Optional[bool] = Field(alias="edgeNoFirstRun", default=None,)

from .windows_kiosk_app_type import WindowsKioskAppType
from .windows_app_start_layout_tile_size import WindowsAppStartLayoutTileSize
from .windows_edge_kiosk_type import WindowsEdgeKioskType
