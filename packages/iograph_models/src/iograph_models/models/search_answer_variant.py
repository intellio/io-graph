from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchAnswerVariant(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	languageTag: Optional[str] = Field(default=None,alias="languageTag",)
	platform: Optional[DevicePlatformType] = Field(default=None,alias="platform",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .device_platform_type import DevicePlatformType

