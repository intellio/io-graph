from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServiceHostedMediaConfig(BaseModel):
	removeFromDefaultAudioGroup: Optional[bool] = Field(alias="removeFromDefaultAudioGroup", default=None,)
	odata_type: Literal["#microsoft.graph.serviceHostedMediaConfig"] = Field(alias="@odata.type", default="#microsoft.graph.serviceHostedMediaConfig")
	liveCaptionOptions: Optional[LiveCaptionOptions] = Field(alias="liveCaptionOptions", default=None,)
	preFetchMedia: Optional[list[MediaInfo]] = Field(alias="preFetchMedia", default=None,)

from .live_caption_options import LiveCaptionOptions
from .media_info import MediaInfo
