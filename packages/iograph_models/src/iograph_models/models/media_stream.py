from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaStream(BaseModel):
	direction: Optional[MediaDirection] = Field(default=None,alias="direction",)
	label: Optional[str] = Field(default=None,alias="label",)
	mediaType: Optional[Modality] = Field(default=None,alias="mediaType",)
	serverMuted: Optional[bool] = Field(default=None,alias="serverMuted",)
	sourceId: Optional[str] = Field(default=None,alias="sourceId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .media_direction import MediaDirection
from .modality import Modality

