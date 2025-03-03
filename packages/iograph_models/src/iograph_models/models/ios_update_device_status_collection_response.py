from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosUpdateDeviceStatusCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[IosUpdateDeviceStatus]] = Field(default=None,alias="value",)

from .ios_update_device_status import IosUpdateDeviceStatus

