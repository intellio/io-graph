from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEmailThreatSubmissionPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityEmailThreatSubmissionPolicy]] = Field(alias="value", default=None,)

from .security_email_threat_submission_policy import SecurityEmailThreatSubmissionPolicy

