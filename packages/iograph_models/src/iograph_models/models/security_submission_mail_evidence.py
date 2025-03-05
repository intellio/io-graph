from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySubmissionMailEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	networkMessageId: Optional[str] = Field(alias="networkMessageId",default=None,)
	recipient: Optional[str] = Field(alias="recipient",default=None,)
	reportType: Optional[str] = Field(alias="reportType",default=None,)
	sender: Optional[str] = Field(alias="sender",default=None,)
	senderIp: Optional[str] = Field(alias="senderIp",default=None,)
	subject: Optional[str] = Field(alias="subject",default=None,)
	submissionDateTime: Optional[datetime] = Field(alias="submissionDateTime",default=None,)
	submissionId: Optional[str] = Field(alias="submissionId",default=None,)
	submitter: Optional[str] = Field(alias="submitter",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

