from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Log_teleconference_device_qualityPostRequest(BaseModel):
	quality: Optional[TeleconferenceDeviceQuality] = Field(default=None,alias="quality",)

from .teleconference_device_quality import TeleconferenceDeviceQuality

