from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementExchangeAccessRule(BaseModel):
	accessLevel: Optional[DeviceManagementExchangeAccessLevel | str] = Field(alias="accessLevel", default=None,)
	deviceClass: Optional[DeviceManagementExchangeDeviceClass] = Field(alias="deviceClass", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_exchange_access_level import DeviceManagementExchangeAccessLevel
from .device_management_exchange_device_class import DeviceManagementExchangeDeviceClass

