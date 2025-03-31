from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityFileContentThreatSubmissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityFileContentThreatSubmission]] = Field(alias="value", default=None,)

from .security_file_content_threat_submission import SecurityFileContentThreatSubmission
