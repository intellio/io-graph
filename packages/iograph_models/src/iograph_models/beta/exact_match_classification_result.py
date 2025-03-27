from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExactMatchClassificationResult(BaseModel):
	classification: Optional[list[ExactMatchDetectedSensitiveContent]] = Field(alias="classification", default=None,)
	errors: Optional[list[ClassificationError]] = Field(alias="errors", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .exact_match_detected_sensitive_content import ExactMatchDetectedSensitiveContent
from .classification_error import ClassificationError

