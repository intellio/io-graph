from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessDeviceUsageSummary(BaseModel):
	activeDeviceCount: Optional[int] = Field(alias="activeDeviceCount", default=None,)
	inactiveDeviceCount: Optional[int] = Field(alias="inactiveDeviceCount", default=None,)
	totalDeviceCount: Optional[int] = Field(alias="totalDeviceCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

