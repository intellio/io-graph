from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaSource(BaseModel):
	contentCategory: Optional[MediaSourceContentCategory | str] = Field(alias="contentCategory", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .media_source_content_category import MediaSourceContentCategory
