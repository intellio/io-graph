from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBlobEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	blobContainer: Optional[SecurityBlobContainerEvidence] = Field(alias="blobContainer",default=None,)
	etag: Optional[str] = Field(alias="etag",default=None,)
	fileHashes: Optional[list[SecurityFileHash]] = Field(alias="fileHashes",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_blob_container_evidence import SecurityBlobContainerEvidence
from .security_file_hash import SecurityFileHash

