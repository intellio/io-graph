from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CallMediaState(BaseModel):
	audio: Optional[str | MediaState] = Field(alias="audio",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .media_state import MediaState

