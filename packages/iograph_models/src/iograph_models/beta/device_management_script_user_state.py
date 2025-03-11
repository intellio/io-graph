from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementScriptUserState(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount",default=None,)
	successDeviceCount: Optional[int] = Field(alias="successDeviceCount",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	deviceRunStates: Optional[list[DeviceManagementScriptDeviceState]] = Field(alias="deviceRunStates",default=None,)

from .device_management_script_device_state import DeviceManagementScriptDeviceState

