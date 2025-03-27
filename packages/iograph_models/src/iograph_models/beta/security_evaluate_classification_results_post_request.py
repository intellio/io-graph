from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_evaluate_classification_resultsPostRequest(BaseModel):
	contentInfo: Optional[SecurityContentInfo] = Field(alias="contentInfo", default=None,)
	classificationResults: Optional[list[SecurityClassificationResult]] = Field(alias="classificationResults", default=None,)

from .security_content_info import SecurityContentInfo
from .security_classification_result import SecurityClassificationResult

