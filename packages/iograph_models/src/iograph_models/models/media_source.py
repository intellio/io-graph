from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaSource(BaseModel):
	contentCategory: Optional[MediaSourceContentCategory] = Field(default=None,alias="contentCategory",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .media_source_content_category import MediaSourceContentCategory

