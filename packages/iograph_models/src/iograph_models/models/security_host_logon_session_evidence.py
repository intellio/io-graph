from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityHostLogonSessionEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	account: Optional[SecurityUserEvidence] = Field(default=None,alias="account",)
	endUtcDateTime: Optional[datetime] = Field(default=None,alias="endUtcDateTime",)
	host: Optional[SecurityDeviceEvidence] = Field(default=None,alias="host",)
	sessionId: Optional[str] = Field(default=None,alias="sessionId",)
	startUtcDateTime: Optional[datetime] = Field(default=None,alias="startUtcDateTime",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_user_evidence import SecurityUserEvidence
from .security_device_evidence import SecurityDeviceEvidence

