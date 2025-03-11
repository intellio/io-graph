from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceConfigurationSettingStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceConfigurationSettingState]] = Field(alias="value",default=None,)

from .device_configuration_setting_state import DeviceConfigurationSettingState

