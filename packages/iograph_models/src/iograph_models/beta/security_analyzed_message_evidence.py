from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAnalyzedMessageEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.analyzedMessageEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.analyzedMessageEvidence")
	antiSpamDirection: Optional[str] = Field(alias="antiSpamDirection", default=None,)
	attachmentsCount: Optional[int] = Field(alias="attachmentsCount", default=None,)
	deliveryAction: Optional[str] = Field(alias="deliveryAction", default=None,)
	deliveryLocation: Optional[str] = Field(alias="deliveryLocation", default=None,)
	internetMessageId: Optional[str] = Field(alias="internetMessageId", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	networkMessageId: Optional[str] = Field(alias="networkMessageId", default=None,)
	p1Sender: Optional[SecurityEmailSender] = Field(alias="p1Sender", default=None,)
	p2Sender: Optional[SecurityEmailSender] = Field(alias="p2Sender", default=None,)
	receivedDateTime: Optional[datetime] = Field(alias="receivedDateTime", default=None,)
	recipientEmailAddress: Optional[str] = Field(alias="recipientEmailAddress", default=None,)
	senderIp: Optional[str] = Field(alias="senderIp", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	threatDetectionMethods: Optional[list[str]] = Field(alias="threatDetectionMethods", default=None,)
	threats: Optional[list[str]] = Field(alias="threats", default=None,)
	urlCount: Optional[int] = Field(alias="urlCount", default=None,)
	urls: Optional[list[str]] = Field(alias="urls", default=None,)
	urn: Optional[str] = Field(alias="urn", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_email_sender import SecurityEmailSender
