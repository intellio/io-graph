from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaPrompt(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	mediaInfo: Optional[MediaInfo] = Field(alias="mediaInfo",default=None,)

from .media_info import MediaInfo

