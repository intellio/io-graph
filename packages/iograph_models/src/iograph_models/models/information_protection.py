from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InformationProtection(BaseModel):
	bitlocker: Optional[Bitlocker] = Field(alias="bitlocker",default=None,)
	threatAssessmentRequests: SerializeAsAny[Optional[list[ThreatAssessmentRequest]]] = Field(alias="threatAssessmentRequests",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .bitlocker import Bitlocker
from .threat_assessment_request import ThreatAssessmentRequest

