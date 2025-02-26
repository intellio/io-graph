from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ThreatAssessmentResult(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	message: Optional[str] = Field(default=None,alias="message",)
	resultType: Optional[ThreatAssessmentResultType] = Field(default=None,alias="resultType",)

from .threat_assessment_result_type import ThreatAssessmentResultType

