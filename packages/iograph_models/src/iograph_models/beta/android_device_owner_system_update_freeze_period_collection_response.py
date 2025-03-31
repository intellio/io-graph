from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidDeviceOwnerSystemUpdateFreezePeriodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidDeviceOwnerSystemUpdateFreezePeriod]] = Field(alias="value", default=None,)

from .android_device_owner_system_update_freeze_period import AndroidDeviceOwnerSystemUpdateFreezePeriod
