from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Send_dtmf_tonesPostRequest(BaseModel):
	tones: Optional[list[Tone | str]] = Field(alias="tones",default=None,)
	delayBetweenTonesMs: Optional[int] = Field(alias="delayBetweenTonesMs",default=None,)
	clientContext: Optional[str] = Field(alias="clientContext",default=None,)

from .tone import Tone

