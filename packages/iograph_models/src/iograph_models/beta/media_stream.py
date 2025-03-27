from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaStream(BaseModel):
	direction: Optional[MediaDirection | str] = Field(alias="direction", default=None,)
	label: Optional[str] = Field(alias="label", default=None,)
	mediaType: Optional[Modality | str] = Field(alias="mediaType", default=None,)
	serverMuted: Optional[bool] = Field(alias="serverMuted", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .media_direction import MediaDirection
from .modality import Modality

