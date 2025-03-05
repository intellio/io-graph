from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySubmissionMailEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	networkMessageId: Optional[str] = Field(default=None,alias="networkMessageId",)
	recipient: Optional[str] = Field(default=None,alias="recipient",)
	reportType: Optional[str] = Field(default=None,alias="reportType",)
	sender: Optional[str] = Field(default=None,alias="sender",)
	senderIp: Optional[str] = Field(default=None,alias="senderIp",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	submissionDateTime: Optional[datetime] = Field(default=None,alias="submissionDateTime",)
	submissionId: Optional[str] = Field(default=None,alias="submissionId",)
	submitter: Optional[str] = Field(default=None,alias="submitter",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

