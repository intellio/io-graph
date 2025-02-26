from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ToneInfo(BaseModel):
	sequenceId: Optional[int] = Field(default=None,alias="sequenceId",)
	tone: Optional[Tone] = Field(default=None,alias="tone",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .tone import Tone

