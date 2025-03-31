from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementIntentDeviceSettingStateSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementIntentDeviceSettingStateSummary]] = Field(alias="value", default=None,)

from .device_management_intent_device_setting_state_summary import DeviceManagementIntentDeviceSettingStateSummary
