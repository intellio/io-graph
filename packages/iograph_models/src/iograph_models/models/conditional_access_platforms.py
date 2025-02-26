from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessPlatforms(BaseModel):
	excludePlatforms: list[ConditionalAccessDevicePlatform] = Field(alias="excludePlatforms",)
	includePlatforms: list[ConditionalAccessDevicePlatform] = Field(alias="includePlatforms",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_device_platform import ConditionalAccessDevicePlatform
from .conditional_access_device_platform import ConditionalAccessDevicePlatform

