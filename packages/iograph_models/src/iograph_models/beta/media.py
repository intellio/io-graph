from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Media(BaseModel):
	isTranscriptionShown: Optional[bool] = Field(alias="isTranscriptionShown",default=None,)
	mediaSource: Optional[MediaSource] = Field(alias="mediaSource",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .media_source import MediaSource

