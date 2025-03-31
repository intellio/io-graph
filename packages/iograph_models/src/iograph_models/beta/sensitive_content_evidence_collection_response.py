from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SensitiveContentEvidenceCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SensitiveContentEvidence]] = Field(alias="value", default=None,)

from .sensitive_content_evidence import SensitiveContentEvidence
