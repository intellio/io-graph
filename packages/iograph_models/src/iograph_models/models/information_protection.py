from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InformationProtection(BaseModel):
	bitlocker: Optional[Bitlocker] = Field(default=None,alias="bitlocker",)
	threatAssessmentRequests: Optional[list[ThreatAssessmentRequest]] = Field(default=None,alias="threatAssessmentRequests",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .bitlocker import Bitlocker
from .threat_assessment_request import ThreatAssessmentRequest

