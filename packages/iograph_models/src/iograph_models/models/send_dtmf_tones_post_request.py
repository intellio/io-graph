from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Send_dtmf_tonesPostRequest(BaseModel):
	tones: Optional[list[Tone]] = Field(default=None,alias="tones",)
	delayBetweenTonesMs: Optional[int] = Field(default=None,alias="delayBetweenTonesMs",)
	clientContext: Optional[str] = Field(default=None,alias="clientContext",)

from .tone import Tone

