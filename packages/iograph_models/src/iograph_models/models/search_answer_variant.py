from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchAnswerVariant(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	languageTag: Optional[str] = Field(alias="languageTag",default=None,)
	platform: Optional[str | DevicePlatformType] = Field(alias="platform",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_platform_type import DevicePlatformType

