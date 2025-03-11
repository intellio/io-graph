from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Evaluate_classification_resultsPostRequest(BaseModel):
	contentInfo: Optional[ContentInfo] = Field(alias="contentInfo",default=None,)
	classificationResults: Optional[list[ClassificationResult]] = Field(alias="classificationResults",default=None,)

from .content_info import ContentInfo
from .classification_result import ClassificationResult

