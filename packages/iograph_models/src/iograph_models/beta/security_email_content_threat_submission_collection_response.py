from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEmailContentThreatSubmissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityEmailContentThreatSubmission]] = Field(alias="value", default=None,)

from .security_email_content_threat_submission import SecurityEmailContentThreatSubmission
