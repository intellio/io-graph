from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessPlatforms(BaseModel):
	excludePlatforms: Optional[list[ConditionalAccessDevicePlatform | str]] = Field(alias="excludePlatforms", default=None,)
	includePlatforms: Optional[list[ConditionalAccessDevicePlatform | str]] = Field(alias="includePlatforms", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_device_platform import ConditionalAccessDevicePlatform
