from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SensitiveContentLocation(BaseModel):
	confidence: Optional[int] = Field(alias="confidence", default=None,)
	evidences: Optional[list[SensitiveContentEvidence]] = Field(alias="evidences", default=None,)
	idMatch: Optional[str] = Field(alias="idMatch", default=None,)
	length: Optional[int] = Field(alias="length", default=None,)
	offset: Optional[int] = Field(alias="offset", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sensitive_content_evidence import SensitiveContentEvidence
