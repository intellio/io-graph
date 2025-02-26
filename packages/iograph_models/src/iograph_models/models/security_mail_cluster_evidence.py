from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityMailClusterEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	clusterBy: Optional[str] = Field(default=None,alias="clusterBy",)
	clusterByValue: Optional[str] = Field(default=None,alias="clusterByValue",)
	emailCount: Optional[int] = Field(default=None,alias="emailCount",)
	networkMessageIds: list[Optional[str]] = Field(alias="networkMessageIds",)
	query: Optional[str] = Field(default=None,alias="query",)
	urn: Optional[str] = Field(default=None,alias="urn",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

