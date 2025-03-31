from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class SecurityThreatSubmissionRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.threatSubmissionRoot"] = Field(alias="@odata.type",)
	emailThreats: Optional[list[Annotated[Union[SecurityEmailContentThreatSubmission, SecurityEmailUrlThreatSubmission],Field(discriminator="odata_type")]]] = Field(alias="emailThreats", default=None,)
	emailThreatSubmissionPolicies: Optional[list[SecurityEmailThreatSubmissionPolicy]] = Field(alias="emailThreatSubmissionPolicies", default=None,)
	fileThreats: Optional[list[Annotated[Union[SecurityFileContentThreatSubmission, SecurityFileUrlThreatSubmission],Field(discriminator="odata_type")]]] = Field(alias="fileThreats", default=None,)
	urlThreats: Optional[list[SecurityUrlThreatSubmission]] = Field(alias="urlThreats", default=None,)

from .security_email_content_threat_submission import SecurityEmailContentThreatSubmission
from .security_email_url_threat_submission import SecurityEmailUrlThreatSubmission
from .security_email_threat_submission_policy import SecurityEmailThreatSubmissionPolicy
from .security_file_content_threat_submission import SecurityFileContentThreatSubmission
from .security_file_url_threat_submission import SecurityFileUrlThreatSubmission
from .security_url_threat_submission import SecurityUrlThreatSubmission
