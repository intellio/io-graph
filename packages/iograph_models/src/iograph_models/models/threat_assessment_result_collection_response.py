from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ThreatAssessmentResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ThreatAssessmentResult] = Field(alias="value",)

from .threat_assessment_result import ThreatAssessmentResult

