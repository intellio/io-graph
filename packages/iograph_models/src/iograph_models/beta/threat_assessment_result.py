from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ThreatAssessmentResult(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.threatAssessmentResult"] = Field(alias="@odata.type", default="#microsoft.graph.threatAssessmentResult")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	resultType: Optional[ThreatAssessmentResultType | str] = Field(alias="resultType", default=None,)

from .threat_assessment_result_type import ThreatAssessmentResultType
