from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementScriptDeviceStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementScriptDeviceState]] = Field(alias="value", default=None,)

from .device_management_script_device_state import DeviceManagementScriptDeviceState
