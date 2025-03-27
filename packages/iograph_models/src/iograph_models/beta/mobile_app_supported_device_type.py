from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppSupportedDeviceType(BaseModel):
	maximumOperatingSystemVersion: Optional[str] = Field(alias="maximumOperatingSystemVersion", default=None,)
	minimumOperatingSystemVersion: Optional[str] = Field(alias="minimumOperatingSystemVersion", default=None,)
	type: Optional[DeviceType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_type import DeviceType

