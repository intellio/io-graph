from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityProcessEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	detectionStatus: Optional[SecurityDetectionStatus] = Field(default=None,alias="detectionStatus",)
	imageFile: Optional[SecurityFileDetails] = Field(default=None,alias="imageFile",)
	mdeDeviceId: Optional[str] = Field(default=None,alias="mdeDeviceId",)
	parentProcessCreationDateTime: Optional[datetime] = Field(default=None,alias="parentProcessCreationDateTime",)
	parentProcessId: Optional[int] = Field(default=None,alias="parentProcessId",)
	parentProcessImageFile: Optional[SecurityFileDetails] = Field(default=None,alias="parentProcessImageFile",)
	processCommandLine: Optional[str] = Field(default=None,alias="processCommandLine",)
	processCreationDateTime: Optional[datetime] = Field(default=None,alias="processCreationDateTime",)
	processId: Optional[int] = Field(default=None,alias="processId",)
	userAccount: Optional[SecurityUserAccount] = Field(default=None,alias="userAccount",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_detection_status import SecurityDetectionStatus
from .security_file_details import SecurityFileDetails
from .security_file_details import SecurityFileDetails
from .security_user_account import SecurityUserAccount

