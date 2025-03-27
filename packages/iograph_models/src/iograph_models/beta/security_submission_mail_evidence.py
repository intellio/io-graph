from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySubmissionMailEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.submissionMailEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.submissionMailEvidence")
	networkMessageId: Optional[str] = Field(alias="networkMessageId", default=None,)
	recipient: Optional[str] = Field(alias="recipient", default=None,)
	reportType: Optional[str] = Field(alias="reportType", default=None,)
	sender: Optional[str] = Field(alias="sender", default=None,)
	senderIp: Optional[str] = Field(alias="senderIp", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	submissionDateTime: Optional[datetime] = Field(alias="submissionDateTime", default=None,)
	submissionId: Optional[str] = Field(alias="submissionId", default=None,)
	submitter: Optional[str] = Field(alias="submitter", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

