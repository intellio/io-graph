from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExactMatchDetectedSensitiveContentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ExactMatchDetectedSensitiveContent]] = Field(alias="value", default=None,)

from .exact_match_detected_sensitive_content import ExactMatchDetectedSensitiveContent
