from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DetectedSensitiveContentWrapper(BaseModel):
	classification: SerializeAsAny[Optional[list[DetectedSensitiveContent]]] = Field(alias="classification",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .detected_sensitive_content import DetectedSensitiveContent

