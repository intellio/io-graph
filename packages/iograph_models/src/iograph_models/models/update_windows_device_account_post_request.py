from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_windows_device_accountPostRequest(BaseModel):
	updateWindowsDeviceAccountActionParameter: Optional[UpdateWindowsDeviceAccountActionParameter] = Field(default=None,alias="updateWindowsDeviceAccountActionParameter",)

from .update_windows_device_account_action_parameter import UpdateWindowsDeviceAccountActionParameter

