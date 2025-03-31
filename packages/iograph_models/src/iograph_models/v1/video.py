from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Video(BaseModel):
	audioBitsPerSample: Optional[int] = Field(alias="audioBitsPerSample", default=None,)
	audioChannels: Optional[int] = Field(alias="audioChannels", default=None,)
	audioFormat: Optional[str] = Field(alias="audioFormat", default=None,)
	audioSamplesPerSecond: Optional[int] = Field(alias="audioSamplesPerSecond", default=None,)
	bitrate: Optional[int] = Field(alias="bitrate", default=None,)
	duration: Optional[int] = Field(alias="duration", default=None,)
	fourCC: Optional[str] = Field(alias="fourCC", default=None,)
	frameRate: float | str | ReferenceNumeric
	height: Optional[int] = Field(alias="height", default=None,)
	width: Optional[int] = Field(alias="width", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric
