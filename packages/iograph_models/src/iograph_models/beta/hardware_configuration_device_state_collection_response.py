from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HardwareConfigurationDeviceStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[HardwareConfigurationDeviceState]] = Field(alias="value", default=None,)

from .hardware_configuration_device_state import HardwareConfigurationDeviceState

