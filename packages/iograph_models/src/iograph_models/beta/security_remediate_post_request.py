from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_remediatePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	severity: Optional[SecurityRemediationSeverity | str] = Field(alias="severity",default=None,)
	action: Optional[SecurityRemediationAction | str] = Field(alias="action",default=None,)
	remediateSendersCopy: Optional[bool] = Field(alias="remediateSendersCopy",default=None,)
	analyzedEmails: Optional[list[SecurityAnalyzedEmail]] = Field(alias="analyzedEmails",default=None,)

from .security_remediation_severity import SecurityRemediationSeverity
from .security_remediation_action import SecurityRemediationAction
from .security_analyzed_email import SecurityAnalyzedEmail

