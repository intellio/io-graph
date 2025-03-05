from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityGitHubOrganizationEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	company: Optional[str] = Field(alias="company",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	login: Optional[str] = Field(alias="login",default=None,)
	orgId: Optional[str] = Field(alias="orgId",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

