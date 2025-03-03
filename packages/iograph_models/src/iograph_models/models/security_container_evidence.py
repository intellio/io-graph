from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityContainerEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	args: Optional[list[str]] = Field(default=None,alias="args",)
	command: Optional[list[str]] = Field(default=None,alias="command",)
	containerId: Optional[str] = Field(default=None,alias="containerId",)
	image: Optional[SecurityContainerImageEvidence] = Field(default=None,alias="image",)
	isPrivileged: Optional[bool] = Field(default=None,alias="isPrivileged",)
	name: Optional[str] = Field(default=None,alias="name",)
	pod: Optional[SecurityKubernetesPodEvidence] = Field(default=None,alias="pod",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_container_image_evidence import SecurityContainerImageEvidence
from .security_kubernetes_pod_evidence import SecurityKubernetesPodEvidence

