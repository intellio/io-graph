from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessPlatforms(BaseModel):
	excludePlatforms: Optional[list[ConditionalAccessDevicePlatform]] = Field(default=None,alias="excludePlatforms",)
	includePlatforms: Optional[list[ConditionalAccessDevicePlatform]] = Field(default=None,alias="includePlatforms",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_device_platform import ConditionalAccessDevicePlatform
from .conditional_access_device_platform import ConditionalAccessDevicePlatform

