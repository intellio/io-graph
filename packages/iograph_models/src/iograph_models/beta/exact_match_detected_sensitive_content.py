from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExactMatchDetectedSensitiveContent(BaseModel):
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	recommendedConfidence: Optional[int] = Field(alias="recommendedConfidence", default=None,)
	uniqueCount: Optional[int] = Field(alias="uniqueCount", default=None,)
	odata_type: Literal["#microsoft.graph.exactMatchDetectedSensitiveContent"] = Field(alias="@odata.type", default="#microsoft.graph.exactMatchDetectedSensitiveContent")
	matches: Optional[list[SensitiveContentLocation]] = Field(alias="matches", default=None,)

from .sensitive_content_location import SensitiveContentLocation
