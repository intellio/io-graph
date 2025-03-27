from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10DeviceFirmwareConfigurationInterfaceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10DeviceFirmwareConfigurationInterface]] = Field(alias="value", default=None,)

from .windows10_device_firmware_configuration_interface import Windows10DeviceFirmwareConfigurationInterface

