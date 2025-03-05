from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallMediaState(BaseModel):
	audio: Optional[MediaState] = Field(default=None,alias="audio",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .media_state import MediaState

