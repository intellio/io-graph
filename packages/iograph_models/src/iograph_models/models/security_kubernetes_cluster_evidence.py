from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityKubernetesClusterEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	cloudResource: SerializeAsAny[Optional[SecurityAlertEvidence]] = Field(default=None,alias="cloudResource",)
	distribution: Optional[str] = Field(default=None,alias="distribution",)
	name: Optional[str] = Field(default=None,alias="name",)
	platform: Optional[SecurityKubernetesPlatform] = Field(default=None,alias="platform",)
	version: Optional[str] = Field(default=None,alias="version",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_alert_evidence import SecurityAlertEvidence
from .security_kubernetes_platform import SecurityKubernetesPlatform

