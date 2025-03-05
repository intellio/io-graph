from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAnalyzedMessageEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	antiSpamDirection: Optional[str] = Field(default=None,alias="antiSpamDirection",)
	attachmentsCount: Optional[int] = Field(default=None,alias="attachmentsCount",)
	deliveryAction: Optional[str] = Field(default=None,alias="deliveryAction",)
	deliveryLocation: Optional[str] = Field(default=None,alias="deliveryLocation",)
	internetMessageId: Optional[str] = Field(default=None,alias="internetMessageId",)
	language: Optional[str] = Field(default=None,alias="language",)
	networkMessageId: Optional[str] = Field(default=None,alias="networkMessageId",)
	p1Sender: Optional[SecurityEmailSender] = Field(default=None,alias="p1Sender",)
	p2Sender: Optional[SecurityEmailSender] = Field(default=None,alias="p2Sender",)
	receivedDateTime: Optional[datetime] = Field(default=None,alias="receivedDateTime",)
	recipientEmailAddress: Optional[str] = Field(default=None,alias="recipientEmailAddress",)
	senderIp: Optional[str] = Field(default=None,alias="senderIp",)
	subject: Optional[str] = Field(default=None,alias="subject",)
	threatDetectionMethods: Optional[list[str]] = Field(default=None,alias="threatDetectionMethods",)
	threats: Optional[list[str]] = Field(default=None,alias="threats",)
	urlCount: Optional[int] = Field(default=None,alias="urlCount",)
	urls: Optional[list[str]] = Field(default=None,alias="urls",)
	urn: Optional[str] = Field(default=None,alias="urn",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_email_sender import SecurityEmailSender
from .security_email_sender import SecurityEmailSender

