from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEmailUrlThreatSubmissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityEmailUrlThreatSubmission]] = Field(alias="value", default=None,)

from .security_email_url_threat_submission import SecurityEmailUrlThreatSubmission

