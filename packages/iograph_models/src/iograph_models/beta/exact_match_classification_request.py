from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExactMatchClassificationRequest(BaseModel):
	contentClassifications: Optional[list[ContentClassification]] = Field(alias="contentClassifications", default=None,)
	sensitiveTypeIds: Optional[list[str]] = Field(alias="sensitiveTypeIds", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	timeoutInMs: Optional[int] = Field(alias="timeoutInMs", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .content_classification import ContentClassification
