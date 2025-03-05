from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityGitHubRepoEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	baseUrl: Optional[str] = Field(alias="baseUrl",default=None,)
	login: Optional[str] = Field(alias="login",default=None,)
	owner: Optional[str] = Field(alias="owner",default=None,)
	ownerType: Optional[str] = Field(alias="ownerType",default=None,)
	repoId: Optional[str] = Field(alias="repoId",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

