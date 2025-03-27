from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContentClassification(BaseModel):
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	matches: Optional[list[MatchLocation]] = Field(alias="matches", default=None,)
	sensitiveTypeId: Optional[str] = Field(alias="sensitiveTypeId", default=None,)
	uniqueCount: Optional[int] = Field(alias="uniqueCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .match_location import MatchLocation

