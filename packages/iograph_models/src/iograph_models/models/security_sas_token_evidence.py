from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecuritySasTokenEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowedIpAddresses: Optional[str] = Field(default=None,alias="allowedIpAddresses",)
	allowedResourceTypes: list[Optional[str]] = Field(alias="allowedResourceTypes",)
	allowedServices: list[Optional[str]] = Field(alias="allowedServices",)
	expiryDateTime: Optional[datetime] = Field(default=None,alias="expiryDateTime",)
	permissions: list[Optional[str]] = Field(alias="permissions",)
	protocol: Optional[str] = Field(default=None,alias="protocol",)
	signatureHash: Optional[str] = Field(default=None,alias="signatureHash",)
	signedWith: Optional[str] = Field(default=None,alias="signedWith",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	storageResource: Optional[SecurityAzureResourceEvidence] = Field(default=None,alias="storageResource",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_azure_resource_evidence import SecurityAzureResourceEvidence

