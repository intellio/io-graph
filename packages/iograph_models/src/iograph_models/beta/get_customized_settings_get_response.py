from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_customized_settingsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementIntentCustomizedSetting]] = Field(alias="value", default=None,)

from .device_management_intent_customized_setting import DeviceManagementIntentCustomizedSetting

