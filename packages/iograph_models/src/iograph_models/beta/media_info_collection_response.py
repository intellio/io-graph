from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MediaInfo]] = Field(alias="value", default=None,)

from .media_info import MediaInfo
