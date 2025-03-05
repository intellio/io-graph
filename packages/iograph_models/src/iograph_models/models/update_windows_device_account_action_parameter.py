from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UpdateWindowsDeviceAccountActionParameter(BaseModel):
	calendarSyncEnabled: Optional[bool] = Field(alias="calendarSyncEnabled",default=None,)
	deviceAccount: SerializeAsAny[Optional[WindowsDeviceAccount]] = Field(alias="deviceAccount",default=None,)
	deviceAccountEmail: Optional[str] = Field(alias="deviceAccountEmail",default=None,)
	exchangeServer: Optional[str] = Field(alias="exchangeServer",default=None,)
	passwordRotationEnabled: Optional[bool] = Field(alias="passwordRotationEnabled",default=None,)
	sessionInitiationProtocalAddress: Optional[str] = Field(alias="sessionInitiationProtocalAddress",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows_device_account import WindowsDeviceAccount

