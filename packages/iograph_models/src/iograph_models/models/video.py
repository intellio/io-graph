from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Video(BaseModel):
	audioBitsPerSample: Optional[int] = Field(default=None,alias="audioBitsPerSample",)
	audioChannels: Optional[int] = Field(default=None,alias="audioChannels",)
	audioFormat: Optional[str] = Field(default=None,alias="audioFormat",)
	audioSamplesPerSecond: Optional[int] = Field(default=None,alias="audioSamplesPerSecond",)
	bitrate: Optional[int] = Field(default=None,alias="bitrate",)
	duration: Optional[int] = Field(default=None,alias="duration",)
	fourCC: Optional[str] = Field(default=None,alias="fourCC",)
	frameRate: float | str | ReferenceNumeric
	height: Optional[int] = Field(default=None,alias="height",)
	width: Optional[int] = Field(default=None,alias="width",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric

