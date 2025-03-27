from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityUrlThreatSubmissionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityUrlThreatSubmission]] = Field(alias="value", default=None,)

from .security_url_threat_submission import SecurityUrlThreatSubmission

