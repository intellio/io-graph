from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCloudLogonSessionEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	account: Optional[SecurityUserEvidence] = Field(default=None,alias="account",)
	browser: Optional[str] = Field(default=None,alias="browser",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	operatingSystem: Optional[str] = Field(default=None,alias="operatingSystem",)
	previousLogonDateTime: Optional[datetime] = Field(default=None,alias="previousLogonDateTime",)
	protocol: Optional[str] = Field(default=None,alias="protocol",)
	sessionId: Optional[str] = Field(default=None,alias="sessionId",)
	startUtcDateTime: Optional[datetime] = Field(default=None,alias="startUtcDateTime",)
	userAgent: Optional[str] = Field(default=None,alias="userAgent",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_user_evidence import SecurityUserEvidence

