from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ToneInfo(BaseModel):
	sequenceId: Optional[int] = Field(alias="sequenceId", default=None,)
	tone: Optional[Tone | str] = Field(alias="tone", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .tone import Tone
