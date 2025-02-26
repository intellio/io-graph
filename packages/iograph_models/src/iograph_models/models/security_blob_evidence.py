from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityBlobEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	blobContainer: Optional[SecurityBlobContainerEvidence] = Field(default=None,alias="blobContainer",)
	etag: Optional[str] = Field(default=None,alias="etag",)
	fileHashes: list[SecurityFileHash] = Field(alias="fileHashes",)
	name: Optional[str] = Field(default=None,alias="name",)
	url: Optional[str] = Field(default=None,alias="url",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_blob_container_evidence import SecurityBlobContainerEvidence
from .security_file_hash import SecurityFileHash

