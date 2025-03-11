from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerKioskModeAppPositionItem(BaseModel):
	item: SerializeAsAny[Optional[AndroidDeviceOwnerKioskModeHomeScreenItem]] = Field(alias="item",default=None,)
	position: Optional[int] = Field(alias="position",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .android_device_owner_kiosk_mode_home_screen_item import AndroidDeviceOwnerKioskModeHomeScreenItem

