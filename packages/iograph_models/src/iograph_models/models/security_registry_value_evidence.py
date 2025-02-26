from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityRegistryValueEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	mdeDeviceId: Optional[str] = Field(default=None,alias="mdeDeviceId",)
	registryHive: Optional[str] = Field(default=None,alias="registryHive",)
	registryKey: Optional[str] = Field(default=None,alias="registryKey",)
	registryValue: Optional[str] = Field(default=None,alias="registryValue",)
	registryValueName: Optional[str] = Field(default=None,alias="registryValueName",)
	registryValueType: Optional[str] = Field(default=None,alias="registryValueType",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict

