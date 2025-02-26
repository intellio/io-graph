from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ExpirationPattern(BaseModel):
	duration: Optional[str] = Field(default=None,alias="duration",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	type: Optional[ExpirationPatternType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .expiration_pattern_type import ExpirationPatternType

