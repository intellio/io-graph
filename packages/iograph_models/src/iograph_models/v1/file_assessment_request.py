from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class FileAssessmentRequest(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	category: Optional[ThreatCategory | str] = Field(alias="category",default=None,)
	contentType: Optional[ThreatAssessmentContentType | str] = Field(alias="contentType",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	expectedAssessment: Optional[ThreatExpectedAssessment | str] = Field(alias="expectedAssessment",default=None,)
	requestSource: Optional[ThreatAssessmentRequestSource | str] = Field(alias="requestSource",default=None,)
	status: Optional[ThreatAssessmentStatus | str] = Field(alias="status",default=None,)
	results: Optional[list[ThreatAssessmentResult]] = Field(alias="results",default=None,)
	contentData: Optional[str] = Field(alias="contentData",default=None,)
	fileName: Optional[str] = Field(alias="fileName",default=None,)

from .threat_category import ThreatCategory
from .threat_assessment_content_type import ThreatAssessmentContentType
from .identity_set import IdentitySet
from .threat_expected_assessment import ThreatExpectedAssessment
from .threat_assessment_request_source import ThreatAssessmentRequestSource
from .threat_assessment_status import ThreatAssessmentStatus
from .threat_assessment_result import ThreatAssessmentResult

