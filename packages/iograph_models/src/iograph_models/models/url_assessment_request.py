from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UrlAssessmentRequest(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	category: Optional[ThreatCategory] = Field(default=None,alias="category",)
	contentType: Optional[ThreatAssessmentContentType] = Field(default=None,alias="contentType",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	expectedAssessment: Optional[ThreatExpectedAssessment] = Field(default=None,alias="expectedAssessment",)
	requestSource: Optional[ThreatAssessmentRequestSource] = Field(default=None,alias="requestSource",)
	status: Optional[ThreatAssessmentStatus] = Field(default=None,alias="status",)
	results: Optional[list[ThreatAssessmentResult]] = Field(default=None,alias="results",)
	url: Optional[str] = Field(default=None,alias="url",)

from .threat_category import ThreatCategory
from .threat_assessment_content_type import ThreatAssessmentContentType
from .identity_set import IdentitySet
from .threat_expected_assessment import ThreatExpectedAssessment
from .threat_assessment_request_source import ThreatAssessmentRequestSource
from .threat_assessment_status import ThreatAssessmentStatus
from .threat_assessment_result import ThreatAssessmentResult

