from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class LocateDeviceActionResult(BaseModel):
	actionName: Optional[str] = Field(alias="actionName", default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Literal["#microsoft.graph.locateDeviceActionResult"] = Field(alias="@odata.type", default="#microsoft.graph.locateDeviceActionResult")
	deviceLocation: Optional[DeviceGeoLocation] = Field(alias="deviceLocation", default=None,)

from .action_state import ActionState
from .device_geo_location import DeviceGeoLocation
