from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityServicePrincipalEvidence(BaseModel):
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	detailedRoles: list[Optional[str]] = Field(alias="detailedRoles",)
	remediationStatus: Optional[SecurityEvidenceRemediationStatus] = Field(default=None,alias="remediationStatus",)
	remediationStatusDetails: Optional[str] = Field(default=None,alias="remediationStatusDetails",)
	roles: list[SecurityEvidenceRole] = Field(alias="roles",)
	tags: list[Optional[str]] = Field(alias="tags",)
	verdict: Optional[SecurityEvidenceVerdict] = Field(default=None,alias="verdict",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	appOwnerTenantId: Optional[str] = Field(default=None,alias="appOwnerTenantId",)
	servicePrincipalName: Optional[str] = Field(default=None,alias="servicePrincipalName",)
	servicePrincipalObjectId: Optional[str] = Field(default=None,alias="servicePrincipalObjectId",)
	servicePrincipalType: Optional[SecurityServicePrincipalType] = Field(default=None,alias="servicePrincipalType",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)

from .security_evidence_remediation_status import SecurityEvidenceRemediationStatus
from .security_evidence_role import SecurityEvidenceRole
from .security_evidence_verdict import SecurityEvidenceVerdict
from .security_service_principal_type import SecurityServicePrincipalType

