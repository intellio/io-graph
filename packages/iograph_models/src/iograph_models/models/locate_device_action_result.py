from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LocateDeviceActionResult(BaseModel):
	actionName: Optional[str] = Field(default=None,alias="actionName",)
	actionState: Optional[ActionState] = Field(default=None,alias="actionState",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceLocation: Optional[DeviceGeoLocation] = Field(default=None,alias="deviceLocation",)

from .action_state import ActionState
from .device_geo_location import DeviceGeoLocation

