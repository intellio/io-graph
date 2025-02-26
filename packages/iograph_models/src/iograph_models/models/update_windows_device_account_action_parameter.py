from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UpdateWindowsDeviceAccountActionParameter(BaseModel):
	calendarSyncEnabled: Optional[bool] = Field(default=None,alias="calendarSyncEnabled",)
	deviceAccount: Optional[WindowsDeviceAccount] = Field(default=None,alias="deviceAccount",)
	deviceAccountEmail: Optional[str] = Field(default=None,alias="deviceAccountEmail",)
	exchangeServer: Optional[str] = Field(default=None,alias="exchangeServer",)
	passwordRotationEnabled: Optional[bool] = Field(default=None,alias="passwordRotationEnabled",)
	sessionInitiationProtocalAddress: Optional[str] = Field(default=None,alias="sessionInitiationProtocalAddress",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .windows_device_account import WindowsDeviceAccount

