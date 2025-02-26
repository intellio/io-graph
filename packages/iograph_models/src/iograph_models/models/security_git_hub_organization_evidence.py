from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityGitHubOrganizationEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	company: Optional[str] = Field(default=None,alias="company",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	email: Optional[str] = Field(default=None,alias="email",)
	login: Optional[str] = Field(default=None,alias="login",)
	orgId: Optional[str] = Field(default=None,alias="orgId",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

