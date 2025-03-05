from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCloudLogonSessionEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	account: Optional[SecurityUserEvidence] = Field(alias="account",default=None,)
	browser: Optional[str] = Field(alias="browser",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem",default=None,)
	previousLogonDateTime: Optional[datetime] = Field(alias="previousLogonDateTime",default=None,)
	protocol: Optional[str] = Field(alias="protocol",default=None,)
	sessionId: Optional[str] = Field(alias="sessionId",default=None,)
	startUtcDateTime: Optional[datetime] = Field(alias="startUtcDateTime",default=None,)
	userAgent: Optional[str] = Field(alias="userAgent",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_user_evidence import SecurityUserEvidence

