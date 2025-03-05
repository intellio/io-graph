from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_windows_device_accountPostRequest(BaseModel):
	updateWindowsDeviceAccountActionParameter: Optional[UpdateWindowsDeviceAccountActionParameter] = Field(alias="updateWindowsDeviceAccountActionParameter",default=None,)

from .update_windows_device_account_action_parameter import UpdateWindowsDeviceAccountActionParameter

