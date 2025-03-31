from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Classify_exact_matchesPostRequest(BaseModel):
	text: Optional[str] = Field(alias="text", default=None,)
	timeoutInMs: Optional[str] = Field(alias="timeoutInMs", default=None,)
	sensitiveTypeIds: Optional[list[str]] = Field(alias="sensitiveTypeIds", default=None,)
	contentClassifications: Optional[list[ContentClassification]] = Field(alias="contentClassifications", default=None,)

from .content_classification import ContentClassification
