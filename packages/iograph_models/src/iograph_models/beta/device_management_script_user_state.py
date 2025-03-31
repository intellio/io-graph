from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceManagementScriptUserState(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceManagementScriptUserState"] = Field(alias="@odata.type",)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	successDeviceCount: Optional[int] = Field(alias="successDeviceCount", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	deviceRunStates: Optional[list[DeviceManagementScriptDeviceState]] = Field(alias="deviceRunStates", default=None,)

from .device_management_script_device_state import DeviceManagementScriptDeviceState
