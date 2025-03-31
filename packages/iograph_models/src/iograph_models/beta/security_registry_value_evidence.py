from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityRegistryValueEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	detailedRoles: Optional[list[str]] = Field(alias="detailedRoles", default=None,)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus | str] = Field(alias="remediationStatus", default=None,)
	remediationStatusDetails: Optional[str] = Field(alias="remediationStatusDetails", default=None,)
	roles: Optional[list[SecurityEvidenceRole | str]] = Field(alias="roles", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	verdict: Optional[SecurityEvidenceVerdict | str] = Field(alias="verdict", default=None,)
	odata_type: Literal["#microsoft.graph.security.registryValueEvidence"] = Field(alias="@odata.type", default="#microsoft.graph.security.registryValueEvidence")
	mdeDeviceId: Optional[str] = Field(alias="mdeDeviceId", default=None,)
	registryHive: Optional[str] = Field(alias="registryHive", default=None,)
	registryKey: Optional[str] = Field(alias="registryKey", default=None,)
	registryValue: Optional[str] = Field(alias="registryValue", default=None,)
	registryValueName: Optional[str] = Field(alias="registryValueName", default=None,)
	registryValueType: Optional[str] = Field(alias="registryValueType", default=None,)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
