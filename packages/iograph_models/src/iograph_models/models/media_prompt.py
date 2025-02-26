from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaPrompt(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	mediaInfo: Optional[MediaInfo] = Field(default=None,alias="mediaInfo",)

from .media_info import MediaInfo

