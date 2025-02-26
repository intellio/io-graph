from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityContainerImageEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	digestImage: Optional[SecurityContainerImageEvidence] = Field(default=None,alias="digestImage",)
	imageId: Optional[str] = Field(default=None,alias="imageId",)
	registry: Optional[SecurityContainerRegistryEvidence] = Field(default=None,alias="registry",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_container_registry_evidence import SecurityContainerRegistryEvidence

