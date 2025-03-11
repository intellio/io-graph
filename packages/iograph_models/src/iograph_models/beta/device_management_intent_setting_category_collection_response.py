from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntentSettingCategoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceManagementIntentSettingCategory]] = Field(alias="value",default=None,)

from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory

