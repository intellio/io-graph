from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceSummarizedAppState(BaseModel):
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	summarizedAppState: Optional[DeviceManagementScriptRunState | str] = Field(alias="summarizedAppState", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_script_run_state import DeviceManagementScriptRunState
