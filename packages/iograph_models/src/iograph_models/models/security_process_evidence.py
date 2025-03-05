from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProcessEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles",default=None,)
	remediationStatus: Optional[str | SecurityEvidenceRemediationStatus] = Field(alias="remediationStatus",default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails",default=None,)
	roles: Optional[list[str | SecurityEvidenceRole]] = Field(alias="roles",default=None,)
	tags: Optional[list[str]] = Field(alias="tags",default=None,)
	verdict: Optional[str | SecurityEvidenceVerdict] = Field(alias="verdict",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	detectionStatus: Optional[str | SecurityDetectionStatus] = Field(alias="detectionStatus",default=None,)
	imageFile: Optional[SecurityFileDetails] = Field(alias="imageFile",default=None,)
	mdeDeviceId: Optional[str] = Field(alias="mdeDeviceId",default=None,)
	parentProcessCreationDateTime: Optional[datetime] = Field(alias="parentProcessCreationDateTime",default=None,)
	parentProcessId: Optional[int] = Field(alias="parentProcessId",default=None,)
	parentProcessImageFile: Optional[SecurityFileDetails] = Field(alias="parentProcessImageFile",default=None,)
	processCommandLine: Optional[str] = Field(alias="processCommandLine",default=None,)
	processCreationDateTime: Optional[datetime] = Field(alias="processCreationDateTime",default=None,)
	processId: Optional[int] = Field(alias="processId",default=None,)
	userAccount: Optional[SecurityUserAccount] = Field(alias="userAccount",default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_detection_status import SecurityDetectionStatus
from .security_file_details import SecurityFileDetails
from .security_file_details import SecurityFileDetails
from .security_user_account import SecurityUserAccount

