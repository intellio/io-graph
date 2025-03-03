from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecuritySasTokenEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: Optional[list[str]] = Field(default=None,alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: Optional[list[SecurityEvidenceRole]] = Field(default=None,alias="roles",)
	tags: Optional[list[str]] = Field(default=None,alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowedIpAddresses: Optional[str] = Field(default=None,alias="allowedIpAddresses",)
	allowedResourceTypes: Optional[list[str]] = Field(default=None,alias="allowedResourceTypes",)
	allowedServices: Optional[list[str]] = Field(default=None,alias="allowedServices",)
	expiryDateTime: Optional[datetime] = Field(default=None,alias="expiryDateTime",)
	permissions: Optional[list[str]] = Field(default=None,alias="permissions",)
	protocol: Optional[str] = Field(default=None,alias="protocol",)
	signatureHash: Optional[str] = Field(default=None,alias="signatureHash",)
	signedWith: Optional[str] = Field(default=None,alias="signedWith",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	storageResource: Optional[SecurityAzureResourceEvidence] = Field(default=None,alias="storageResource",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_azure_resource_evidence import SecurityAzureResourceEvidence

