from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceMobileAppConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ManagedDeviceMobileAppConfiguration]] = Field(default=None,alias="value",)

from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

