from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityThreatSubmissionRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	emailThreats: SerializeAsAny[Optional[list[SecurityEmailThreatSubmission]]] = Field(alias="emailThreats",default=None,)
	emailThreatSubmissionPolicies: Optional[list[SecurityEmailThreatSubmissionPolicy]] = Field(alias="emailThreatSubmissionPolicies",default=None,)
	fileThreats: SerializeAsAny[Optional[list[SecurityFileThreatSubmission]]] = Field(alias="fileThreats",default=None,)
	urlThreats: Optional[list[SecurityUrlThreatSubmission]] = Field(alias="urlThreats",default=None,)

from .security_email_threat_submission import SecurityEmailThreatSubmission
from .security_email_threat_submission_policy import SecurityEmailThreatSubmissionPolicy
from .security_file_threat_submission import SecurityFileThreatSubmission
from .security_url_threat_submission import SecurityUrlThreatSubmission

