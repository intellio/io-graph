from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceHostedMediaConfig(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	preFetchMedia: list[MediaInfo] = Field(alias="preFetchMedia",)

from .media_info import MediaInfo

