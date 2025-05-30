from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceWindowsOperatingSystemImageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedDeviceWindowsOperatingSystemImage]] = Field(alias="value", default=None,)

from .managed_device_windows_operating_system_image import ManagedDeviceWindowsOperatingSystemImage
