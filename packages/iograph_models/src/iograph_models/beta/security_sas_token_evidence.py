from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySasTokenEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.sasTokenEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.sasTokenEvidence")
	allowedIpAddresses: Optional[str] = Field(alias="allowedIpAddresses", default=None,)
	allowedResourceTypes: Optional[list[str]] = Field(alias="allowedResourceTypes", default=None,)
	allowedServices: Optional[list[str]] = Field(alias="allowedServices", default=None,)
	expiryDateTime: Optional[datetime] = Field(alias="expiryDateTime", default=None,)
	permissions: Optional[list[str]] = Field(alias="permissions", default=None,)
	protocol: Optional[str] = Field(alias="protocol", default=None,)
	signatureHash: Optional[str] = Field(alias="signatureHash", default=None,)
	signedWith: Optional[str] = Field(alias="signedWith", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	storageResource: Optional[SecurityAzureResourceEvidence] = Field(alias="storageResource", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_azure_resource_evidence import SecurityAzureResourceEvidence

