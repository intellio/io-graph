from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeleconferenceDeviceMediaQualityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[TeleconferenceDeviceMediaQuality]] = Field(default=None,alias="value",)

from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

