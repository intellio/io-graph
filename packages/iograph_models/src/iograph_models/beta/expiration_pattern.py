from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExpirationPattern(BaseModel):
	duration: Optional[str] = Field(alias="duration",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	type: Optional[ExpirationPatternType | str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .expiration_pattern_type import ExpirationPatternType

