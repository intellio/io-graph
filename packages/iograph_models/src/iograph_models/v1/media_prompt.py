from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class MediaPrompt(BaseModel):
	odata_type: Literal["#microsoft.graph.mediaPrompt"] = Field(alias="@odata.type", default="#microsoft.graph.mediaPrompt")
	mediaInfo: Optional[MediaInfo] = Field(alias="mediaInfo", default=None,)

from .media_info import MediaInfo

